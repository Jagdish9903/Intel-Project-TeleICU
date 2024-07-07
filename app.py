import streamlit as st
import cv2
from ultralytics import YOLO
import os
from moviepy.editor import VideoFileClip
import datetime

# Load the YOLO model
model_path = 'icu_show_images_model.pt'
model = YOLO(model_path)

# Global variable to store bounding boxes
global_boxes = None

# Define colors for different classes
class_colors = {
    0: (245, 135, 66),   # doctor
    1: (13, 13, 212),   # patient
    2: (250, 26, 128),   # person
    # Add more colors if you have more classes
}

def process_frame(frame, frame_index):
    global global_boxes
    
    if frame_index % 4 == 0:
        try:
            results = model.predict(source=frame, conf=0.25)
            global_boxes = results[0].boxes
        except Exception as e:
            print(f"Error processing frame: {e}")
            global_boxes = None

    if global_boxes is not None:
        for i in range(len(global_boxes)):
            # Extract the coordinates and confidence score
            x1, y1, x2, y2 = map(int, global_boxes.xyxy[i])
            conf = global_boxes.conf[i]
            cls = int(global_boxes.cls[i])

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

def process_video(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        st.error("Error opening video file.")
        return

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    try:
        frame_index = 0
        progress_bar = st.progress(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            annotated_frame = process_frame(frame, frame_index)
            out.write(annotated_frame)
            frame_index += 1
            progress_bar.progress(frame_index / frame_count)
    except Exception as e:
        st.error(f"Error processing frames: {e}")
    finally:
        cap.release()
        out.release()
    return output_path

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
    output_video_path = 'processed_video_' + str(datetime.datetime.now().strftime("%H%M%S")) + '.mp4'
    processed_video_path = process_video(video_path, output_video_path)

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
        st.header("Processed Video")
        clip.write_videofile(output_file, codec="libx264")
        st.video(output_file)

        st.success(f"Processed video saved to: {processed_video_path}")

