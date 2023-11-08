import streamlit as st
from Back_End import *
import matplotlib.pyplot as plt
from PIL import Image
import io
import time
import shutil
from numpy import nan

# Preconf
st.set_page_config(
    page_title="Pytoshop",
    layout="wide"
)

def params():
    with st.sidebar:
        st.title("Parameters")

        apply_geometric_transformations = st.checkbox("Apply Geometric Transformations")
        with st.expander("Geometric Transformations"):
            rotation = st.slider("Rotation", 0, 100, 1)
            shift = st.slider("Shift", 0, 100, 1)
            scale = st.slider("Scale", 0, 100, 1)
            elastic = st.slider("Elastic", 0, 100, 1)

        apply_color_space_transformations = st.checkbox("Apply Color Space Transformations")
        with st.expander("Color Space Transformations"):
            hue = st.slider("Hue", 0, 100, 1)
            rgbs = st.slider("RGBs", 0, 100, 1)
            brightness = st.slider("Brightness", 0, 100, 1)
            shuffle = st.slider("Shuffle", 0, 100, 1)
            cla = st.slider("Cla", 0, 100, 1)

        apply_kernel_filters = st.checkbox("Apply Kernel Filters")
        with st.expander("Kernel Filters"):
            blur = st.slider("Blur", 0, 100, 1)
            meblur = st.slider("MeBlur", 0, 100, 1)
            gaublur = st.slider("GauBlur", 0, 100, 1)
            motion = st.slider("Motion", 0, 100, 1)
            emboss = st.slider("Emboss", 0, 100, 1)

        download_output = st.checkbox("Download the output as a zip file")

        params = [rotation, shift, scale, elastic, hue, rgbs, brightness, shuffle, cla, blur, meblur, gaublur, motion, emboss]
        
        for param in params:
            if param != nan:
                param /= 10

    if download_output:
        download()


def upload():
    uploaded_file = st.file_uploader("Choose your images...", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    if uploaded_file is not None:
        col1, col2, col3 = st.columns(3)
        for idx, file in enumerate(uploaded_file):
            image = Image.open(io.BytesIO(file.read()))
            if idx % 3 == 0:
                col1.image(image, caption=file.name)
            elif idx % 3 == 1:
                col2.image(image, caption=file.name)
            else:
                col3.image(image, caption=file.name)


def download():
    pass

def zip():
    pass


def main():
    st.image("logo.jpg", width=200)
    st.title("Pytoshop - Image Augmentation")\
    
    params()
    upload()

    if st.button("Apply Transformations") == 1:
        pass
        

if __name__ == "__main__":
    main()