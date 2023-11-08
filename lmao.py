import streamlit as st
from Back_End import *
import matplotlib.pyplot as plt
from PIL import Image
import io
import time
import shutil

# Preconf
st.set_page_config(
    page_title="Pytoshop",
    layout="wide"
)

def params():
    with st.sidebar:
        st.title("Parameters")

        with st.expander("Geometric Transformations"):
            st.slider("Rotation", 0, 360, 180)
            st.slider("Shear", 0, 360, 180)
            st.slider("Zoom", 0, 360, 180)
            st.slider("Flip", 0, 360, 180)
            st.slider("Crop", 0, 360, 180)
            

        st.checkbox("Apply All")

        st.checkbox("Download the output as a zip file")


def upload():
    uploaded_file = st.file_uploader("Choose your images...", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    # if uploaded_file is not None:
    #     image = Image.open(uploaded_file)
    #     st.image(image, caption='Uploaded Image.', use_column_width=True)


# def download():
#     st.title("Download")
#     st.write("Download your augmented images here!")
#     st.write("")


# def zip():
#     st.title("Download")
#     st.write("Download your augmented images here!")
#     st.write("")


def main():
    st.image("logo.jpg", width=200)
    st.title("Pytoshop - Image Augmentation")

    params()
    upload()
    # download()




if __name__ == "__main__":
    main()