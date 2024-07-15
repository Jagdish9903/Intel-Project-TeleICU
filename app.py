import streamlit as st
import cv2
from ultralytics import YOLO
import os
from moviepy.editor import VideoFileClip
import datetime
import mediapipe as mp
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

# Load the YOLO model
model_path = 'icu_show_images_model.pt'
model = YOLO(model_path)

model2 = tf.keras.models.load_model('action_30.h5')

mp_holistic = mp.solutions.holistic # Holistic model
mp_drawing = mp.solutions.drawing_utils # Drawing utilities

# Global variable to store bounding boxes
global_boxes = None
cap =   None
width = 848
height = 384
fps = 24

colors = [(245,117,16), (117,245,16), (16,117,245)]
def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        cv2.rectangle(output_frame, (0,60+num*40), (int(prob*100), 90+num*40), colors[num], -1)
        cv2.putText(output_frame, actions[num], (0, 85+num*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)

    return output_frame

# Define colors for different classes
class_colors = {
    0: (245, 135, 66),   # doctor
    1: (13, 13, 212),    # patient
    2: (250, 26, 128),   # person
    # Add more colors if you have more classes
}

colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245), (255,0,0)]

res = None
image = None
results = None
action = None

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_TESSELATION,
                             mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1),
                             mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)
                             )
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             )
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2)
                             )
    # Draw right hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
                             )

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    face = np.array([[res.x, res.y, res.z] for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, face, lh, rh])

def plot_activity_graph(activity_data):
    df = pd.DataFrame(activity_data, columns=['Timestamp', 'Activity', 'Probability'])
    
    # Normalize probabilities to 0-100%
    df['Probability'] = df['Probability'] * 100

    fig, ax = plt.subplots()
    
    # Assign unique colors to each activity
    activity_colors = {
        'Clapping': 'blue',
        'Sitting': 'green',
        'Standing Still': 'orange',
        'Walking': 'red'
    }

    for activity in df['Activity'].unique():
        activity_data = df[df['Activity'] == activity]
        ax.plot(activity_data['Timestamp'], activity_data['Probability'], marker='o', color=activity_colors[activity], label=activity)

    plt.xlabel('Time (s)')
    plt.ylabel('Activity Probability (%)')
    plt.title('Activity Detection Probability Over Time')
    plt.ylim(0, 100)
    plt.legend()
    st.pyplot(fig)


# Function to save video
def save_video(input_path, output_path, model, actions, threshold=0.8):

    activity_data = []

    # Initialize MediaPipe holistic model
    mp_holistic = mp.solutions.holistic

    # Capture video from the provided file path
    cap = cv2.VideoCapture(input_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    fourcc3 = cv2.VideoWriter_fourcc(*'mp4v')
    out3 = cv2.VideoWriter(output_path, fourcc3, fps, (width, height))

    # Initialize sequence and sentence variables
    sequence = []
    sentence = []

    with mp_holistic.Holistic(min_detection_confidence=0.3, min_tracking_confidence=0.3) as holistic:
        frame_idx=0
        media_idx = 0
        while cap.isOpened():
            global results
            global image
            ret, frame = cap.read()
            if not ret:
                break

            # Make detections
            if media_idx % 4 == 0:
              image, results = mediapipe_detection(frame, holistic)

            # Draw landmarks
            # draw_styled_landmarks(image, results)

            # Prediction logic
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-30:]

            if len(sequence) == 30:
                global res
                global action
                if frame_idx % 4 == 0:
                    res = model.predict(np.expand_dims(sequence, axis=0))[0]
                    action = actions[np.argmax(res)]
                    timestamp = frame_idx / fps
                    highest_prob = res[np.argmax(res)]
                    activity_data.append((timestamp, action, highest_prob))

                # Viz logic
                if res[np.argmax(res)] > threshold:
                    if len(sentence) > 0:
                        if action != sentence[-1]:
                            sentence.append(action)
                    else:
                        sentence.append(action)

                if len(sentence) > 5:
                    sentence = sentence[-5:]

                # Viz probabilities
                image = prob_viz(res, actions, image, colors)

                frame_idx += 1

            # Add the sentence to the frame
            cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
            cv2.putText(image, ' '.join(sentence), (3, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

            # Write the frame to the output video
            out3.write(image)

            media_idx += 1

        cap.release()
        out3.release()
        cv2.destroyAllWindows()

    return output_path, activity_data

pat = []
cropped_frame = None

def process_frame(frame, frame_index, patient_output_path):
    global global_boxes

    if frame_index % 4 == 0:
        try:
            results = model.predict(source=frame, conf=0.25)
            global_boxes = results[0].boxes  # Update to use 'pred' instead of 'boxes'
        except Exception as e:
            print(f"Error processing frame: {e}")
            global_boxes = None
    if global_boxes is not None:
        x1 = -1
        y1 = -1
        x2 = -1
        y2 = -1
        for i in range(len(global_boxes)):
            global cropped_frame
            # Extract the coordinates and confidence score
            min_x1, min_y1, max_x2, max_y2 = map(int, global_boxes.xyxy[i])
            if x1 == -1:
                x1 = min_x1
            else:
                if(abs(x1 - min_x1) > int(width * 0.1)):
                    x1 = min_x1
            if x2 == -1:
                x2 = max_x2
            else:
                if(abs(x2 - max_x2) > int(width * 0.1)):
                    x2 = max_x2
            if y1 == -1:
                y1 = min_y1
            else:
                if(abs(y1 - min_y1) > int(height * 0.1)):
                    y1 = min_y1
            if y2 == -1:
                y2 = max_y2
            else:
                if(abs(y2 - max_y2) > int(height * 0.1)):
                    y2 = max_y2
            
            conf = global_boxes.conf[i]
            cls = int(global_boxes.cls[i])
            # print(global_boxes[i])
            # print(cls)
            # a = input()
            if cls == 1 and cropped_frame != None:
                cropped_frame = frame[y1:y2, x1:x2]
                cropped_frame = cv2.resize(cropped_frame, (width, height))
                # cv2.imwrite("Patient"+str(frame_index)+".jpg", cropped_frame)
                out2.write(cropped_frame)

            # Define the label and color
            label = f"{model.names[cls]}: {conf:.2f}"
            color = class_colors.get(cls, (255, 255, 255))  # Default to white if class color is not defined

            # Draw the bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Calculate the position for the label
            label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.85, 2)
            label_y = y1 - 12 if y1 - 12 > 12 else y1 + 8 + label_size[1]

            # Ensure the label does not go off-screen
            if label_y + label_size[1] > frame.shape[0]:
                label_y = frame.shape[0] - label_size[1]
            if x1 + label_size[0] > frame.shape[1]:
                x1 = frame.shape[1] - label_size[0]

            # Draw the label
            cv2.rectangle(frame, (x1, label_y - label_size[1] - 5), (x1 + label_size[0], label_y + base_line), color, -1)
            cv2.putText(frame, label, (x1, label_y), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 1)
    
    return frame

def process_videos(video_path, output_path, patient_output_path):
    global global_boxes
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error("Error opening video file.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    # print(width)
    # print(height)
    # print(fps)
    # a = input()

    fourcc2 = cv2.VideoWriter_fourcc(*'XVID')
    out2 = cv2.VideoWriter("Patients_cut_video.avi", fourcc2, int(fps), (width, height))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    try:
        frame_index = 0
        progress_bar = st.progress(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            annotated_frame = process_frame(frame, frame_index, patient_output_path)
            out.write(annotated_frame)

            frame_index += 1
            progress_bar.progress(frame_index / frame_count)
    except Exception as e:
        st.error(f"Error processing frames: {e}")
    finally:
        cap.release()
        out.release()
        out2.release()
    return output_path, patient_output_path

# Streamlit UI
st.title('Video Processing with YOLO')
uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

if uploaded_file is not None:
    placeholder = st.empty()
    placeholder.write("Processing...")

    # Save the uploaded video temporarily
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    video_path = os.path.join(temp_dir, uploaded_file.name)
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    # Process the video
    output_video_path = f'processed_video_{datetime.datetime.now().strftime("%H%M%S")}.mp4'
    patient_output_video_path = f'patient_video_{datetime.datetime.now().strftime("%H%M%S")}.mp4'
    # if not os.path.exists(patient_output_video_path):
    #     os.makedirs(patient_output_video_path)
    processed_video_path, processed_patient_video_path = process_videos(video_path, output_video_path, patient_output_video_path)

    placeholder.empty()
    p2 = st.empty()
    p2.write("Processing... done!")

    # Display the processed video if it exists
    if os.path.exists(processed_video_path):
        input_file = processed_video_path
        output_file = processed_video_path[:-4] + '.mkv'

        clip = VideoFileClip(input_file)

        # Convert the video to H.264 codec
        p2.empty()
        st.header("People Identification Video")
        clip.write_videofile(output_file, codec="libx264")
        st.video(output_file)

        st.success(f"People Identification video saved to: {processed_video_path}")

    # Path to input and output videos
    input_path = 'Patients_video_second.avi'
    output_path = 'vid_walk_gpu10.mp4'
    actions = np.array(['Clapping', 'Sitting', 'Standing Still','Walking'])

    pat = st.empty()
    pat.header("Processing Patient's Activity Video...")

    processed_video_path, activity_data = save_video(video_path, patient_output_video_path, model2, actions)

    print("you got it!")
    
    # new patient only frame
    if os.path.exists(processed_video_path):
        input_file = processed_video_path
        output_file = processed_video_path[:-4] + '.mkv'

        clip = VideoFileClip(input_file)

        # Convert the video to H.264 codec
        p2.empty()
        pat.header("Patient's Activity Video")
        clip.write_videofile(output_file, codec="libx264")
        st.video(output_file)

        st.success(f"Patient's Activity Video saved to: {processed_video_path}")
    
    st.header("Activity Detection Over Time")
    plot_activity_graph(activity_data)