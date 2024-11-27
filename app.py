import cv2
import streamlit as st
import numpy as np
from PIL import Image

# Load Haar cascades
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Streamlit app title
import streamlit as st

st.title("Webcam Capture Alternative")

st.markdown("""
    <script>
    function captureAndUpload() {
        const video = document.createElement('video');
        navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
            video.srcObject = stream;
            video.play();
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            canvas.width = 640; 
            canvas.height = 480;
            ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
            canvas.toBlob((blob) => {
                const file = new File([blob], "webcam_capture.jpg", { type: "image/jpeg" });
                const dataTransfer = new DataTransfer();
                dataTransfer.items.add(file);
                const input = document.querySelector("input[type='file']");
                input.files = dataTransfer.files;
            });
            video.srcObject.getTracks().forEach(track => track.stop());
        });
    }
    </script>
""")

st.markdown('<button onclick="captureAndUpload()">Capture from Webcam</button>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload or capture an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Captured or Uploaded Image")
