import albumentations as A
import cv2
import os
import random
def read_img(path):
    path = os.path.join(os.path.join(os.path.dirname(__file__), path))
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def output_img(image, num, output="output"):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    output = os.path.join(os.path.join(os.path.dirname(__file__), output))
    cv2.imwrite("img" + num + ".jpg",image)


def apply_geometric_transform(image):
    angle = random.randint(1,180)
    transform = A.Compose([
        A.Rotate(limit=angle, p=1),
        A.ShiftScaleRotate(p=1),
        A.RandomScale(p=1),
        A.ElasticTransform(p=1),
    ])
    augmented = transform(image=image)
    transformed_image = augmented['image']
    return transformed_image


def color_space_transformations(image):
    transform = A.Compose([
        A.HueSaturationValue(p=0.2),
        A.RGBShift(r_shift_limit=25, g_shift_limit=25, b_shift_limit=25, p=0.2),
        A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.2),
        A.ChannelShuffle(p=0.2),
        A.CLAHE(p=0.2),
    ])

    transformed = transform(image=image)['image']

    return transformed
def kernel_filters(image):
    transform = A.Compose([
        A.Blur(blur_limit=(1, 3)),
        A.MedianBlur(blur_limit=3),
        A.GaussianBlur(blur_limit=3),
        A.MotionBlur(blur_limit=3),
        A.Emboss(alpha=(0.5, 1.0), strength=(1.0, 2.0)),
    ])

    transformed = transform(image=image)['image']

    return transformed
def main():
    for i in range(100):
        image = read_img("314218660_458182969777595_2920542176920776199_n.jpg")
        transformation_functions = [apply_geometric_transform, color_space_transformations, kernel_filters]
        selected_functions = random.sample(transformation_functions, random.randint(0,2)) 
        for function in selected_functions:
            image = function(image)
        output_img(image,str(i))
main()