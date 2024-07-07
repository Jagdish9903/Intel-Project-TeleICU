import streamlit as st
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import cv2
from ultralytics import YOLO
import os
import datetime
import time

# Load the YOLO model
model_path = 'icu_show_images_model.pt'
model = YOLO(model_path)

def process_frame(frame):
    try:
        results = model.predict(source=frame, conf=0.25)
        annotated_frame = results[0].plot()
        return annotated_frame
    except Exception as e:
        print(f"Error processing frame: {e}")
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

    frames = []
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    num_cores = min(cpu_count() - 2, 6)  # Use up to 5 or 6 cores, leaving some for the system
    with Pool(num_cores) as pool:
        for annotated_frame in tqdm(pool.imap(process_frame, frames), total=frame_count, desc="Processing Frames"):
            out.write(annotated_frame)

    out.release()
    os.remove(video_path)
    st.success(f"Processed video saved to: {output_path}")
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
    st.write("Processing... done!")
