import streamlit as st
import cv2
import tempfile
from io import BytesIO
from PIL import Image
import numpy as np

f = st.file_uploader("Upload file")
tfile = tempfile.NamedTemporaryFile(delete=False)
try:
    tfile.write(f.read())
    cap = cv2.VideoCapture(tfile.name)
    frames = []
    while True:
        rat, frame = cap.read()
        if not rat:
                break
        frames.append(frame)

    curr_im = st.slider('Frame', 0, len(frames) - 1, 0)
    st.image(frames[curr_im])
    pred_ar_int = frames[curr_im].astype(np.uint8)
    im = Image.fromarray(pred_ar_int)
    with BytesIO() as ff:
        im.save(ff, format='PNG')
        data = ff.getvalue()
    st.download_button('Save', data, f'{f.name.split(".")[0]}.png', mime="image/png")
except:
    pass