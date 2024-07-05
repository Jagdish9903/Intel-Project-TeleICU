import streamlit as st
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import cv2
from ultralytics import YOLO
import os
import tempfile
from datetime import datetime

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

def process_video(video_file, output_path):
    with open(video_file.name, 'wb') as f:
        f.write(video_file.read())

    cap = cv2.VideoCapture(video_file.name)
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
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(process_frame, frame) for frame in frames]
        for future in tqdm(as_completed(futures), total=frame_count, desc="Processing Frames"):
            annotated_frame = future.result()
            out.write(annotated_frame)

    out.release()

    os.remove(video_file.name)
    st.success(f"Processed video saved to: {output_path}")
    return output_path

# Streamlit UI
st.title('ICU Video Processing with YOLOv8')
uploaded_file = st.file_uploader("Upload a video", type=["mp4"])

if uploaded_file is not None:
    processing_placeholder = st.empty()
    processing_placeholder.write("Processing...")

    # Process the video
    timestamp = datetime.now().strftime('%H%M%S')
    output_video_path = 'processed_video_' + timestamp + '.mp4'
    processed_video_path = process_video(uploaded_file, output_video_path)

    processing_placeholder.empty()