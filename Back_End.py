import albumentations as A
import cv2
import os
import random
import os
import uuid


def read_img(path):
    path = os.path.join(os.path.join(os.path.dirname(__file__), path))
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def output_img(image, num, output="output"):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    output_dir = os.path.join(os.path.dirname(__file__), output)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_path = os.path.join(output_dir, f"{str(uuid.uuid4())}" + ".jpg")
    cv2.imwrite(output_path, image)


def apply_geometric_transform(image, rotate, shift, scale, elastic):
    angle = random.randint(1, 360)
    transform = A.Compose(
        [
            A.Rotate(limit=angle, p=rotate),
            A.ShiftScaleRotate(p=shift),
            A.RandomScale(p=scale),
            A.ElasticTransform(p=elastic),
        ]
    )
    augmented = transform(image=image)
    transformed_image = augmented["image"]
    return transformed_image


def color_space_transformations(image, Hue, RGBs, Brightness, shuffle, Cla):
    transform = A.Compose(
        [
            A.HueSaturationValue(p=Hue),
            A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=RGBs),
            A.RandomBrightnessContrast(
                brightness_limit=0.2, contrast_limit=0.2, p=Brightness
            ),
            A.ChannelShuffle(p=shuffle),
            A.CLAHE(p=Cla),
        ]
    )

    transformed = transform(image=image)["image"]

    return transformed


def kernel_filters(image, blur, meblur, gaublur, motion, emboss):
    transform = A.Compose(
        [
            A.Blur(blur_limit=(1, 3), p=blur),
            A.MedianBlur(blur_limit=3, p=meblur),
            A.GaussianBlur(blur_limit=3, p=gaublur),
            A.MotionBlur(blur_limit=3, p=motion),
            A.Emboss(alpha=(0.5, 1.0), strength=(1.0, 2.0), p=emboss),
        ]
    )

    transformed = transform(image=image)["image"]

    return transformed


def back_end(
    path,
    number_of_images=10,
    transformation_functions=[
        apply_geometric_transform,
        color_space_transformations,
        kernel_filters,
    ],
    
    rotate=0.5,
    shift=0.5,
    scale=0.5,
    elastic=0.5,
    blur=0.5,
    meblur=0.5,
    gaublur=0.5,
    motion=0.5,
    emboss=0.5,
    Hue=0.5,
    RGBs=0.5,
    Brightness=0.5,
    shuffle=0.5,
    Cla=0.5,
):
    for i in range(number_of_images):
        image = read_img(path)
        selected_functions = random.sample(
            transformation_functions,
            random.randint(0, len(transformation_functions) - 1),
        )
        for function in selected_functions:
            if function == apply_geometric_transform:
                image = apply_geometric_transform(image, rotate, shift, scale, elastic)
            elif function == color_space_transformations:
                image = color_space_transformations(
                    image, Hue, RGBs, Brightness, shuffle, Cla
                )
            else:
                image = kernel_filters(image,blur,meblur,gaublur,motion,emboss)
        output_img(image,str(i))
back_end("314218660_458182969777595_2920542176920776199_n.jpg")