from nicegui import events, ui
from nicegui.events import ValueChangeEventArguments
from Back_End import *
import matplotlib.pyplot as plt
from PIL import Image
import io
import uuid
import shutil
import glob
import os

# import pygetwindow as gw

img_folder = "img"
if not os.path.exists(img_folder):
    os.makedirs(img_folder)


def remove_all_files(folder_path):
    files = glob.glob(os.path.join(folder_path, "*"))
    for f in files:
        os.remove(f)


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


with ui.row():
    dark = ui.dark_mode()
    ui.label("Switch mode:")
    ui.button("Dark", on_click=dark.enable)
    ui.button("Light", on_click=dark.disable)
    ui.label("Image Augmentation").classes("text-2xl font-bold text-left")


with ui.card().classes("w-full items-center"):
    with ui.dialog().props("full-width") as dialog:
        with ui.card():
            content = ui.image()

    def handle_upload(e: events.UploadEventArguments):
        img = Image.open(io.BytesIO(e.content.read()))
        # plt.imshow(img)
        # plt.show()
        img_path = os.path.join(img_folder, f"{str(uuid.uuid4())}.jpg")
        img.save(img_path)

    ui.upload(multiple=True, on_upload=handle_upload).props("accept=image/*").classes(
        "max-w-full"
    )

    with ui.column():
        # ui.checkbox("apply_geometric_transform", on_change=show)
        # slider = ui.slider(min=0, max=100, value=50)
        # ui.label().bind_text_from(slider, "value")
        # ui.checkbox("color_space_transformations", on_change=show)
        # ui.checkbox("kernel_filters", on_change=show)
        with ui.expansion("Geometric Transformations"):
            ui.label("Rotate")
            rotateA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(rotateA, "value")

            ui.label("Shift")
            shiftA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(shiftA, "value")

            ui.label("Scale")
            scaleA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(scaleA, "value")

            ui.label("Elastic")
            elasticA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(elasticA, "value")
        with ui.expansion("Kernel Filters"):
            ui.label("Blur")
            blurA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(blurA, "value")

            ui.label("MEBlur")
            meblurA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(meblurA, "value")

            ui.label("GauBlur")
            gaublurA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(gaublurA, "value")

            ui.label("Motion")
            motionA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(motionA, "value")

            ui.label("Emboss")
            embossA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(embossA, "value")

        with ui.expansion("Color Space Transformations"):
            ui.label("Hue")
            HueA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(HueA, "value")

            ui.label("RGBs")
            RGBsA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(RGBsA, "value")

            ui.label("Brightness")
            BrightnessA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(BrightnessA, "value")

            ui.label("Shuffle")
            ShuffleA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(ShuffleA, "value")

            ui.label("Cla")
            ClaA = ui.slider(min=0, max=1, value=0.5, step=0.01)
            ui.label().bind_text_from(ClaA, "value")
        # ui.button('Choose',on_click=lambda: show_numimg())
        # label = ui.label()
        NumberOfImages = ui.number(
            label="Number of Images", value=10, min=1, max=100, step=1
        )

        def showVal(NumberOfImages):
            internal_var = NumberOfImages.value
            print(internal_var)
            return internal_var

        ui.button(
            "Apply Transformations",
            on_click=lambda: apply_imgAug_to_all_images_in_folder(
                os.path.join(os.path.dirname(__file__), "img")
            ),
        )

    def apply_imgAug_to_all_images_in_folder(folder_path):
        # timestamp = ui.spinner("facebook", size="lg", color="green").classes(
        #     "items-center w-full"
        # )
        remove_all_files("output")
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(folder_path, filename)
                    back_end(
                        image_path,
                        number_of_images=int(showVal(NumberOfImages)),
                        rotate=showVal(rotateA),
                        shift=showVal(shiftA),
                        scale=showVal(scaleA),
                        elastic=showVal(elasticA),
                        blur=showVal(blurA),
                        meblur=showVal(meblurA),
                        gaublur=showVal(gaublurA),
                        motion=showVal(motionA),
                        emboss=showVal(embossA),
                        Hue=showVal(HueA),
                        RGBs=showVal(RGBsA),
                    )  # Pass image_path instead of img
                    # ui.notify(f"Success with {filename}", type="positive")
            shutil.make_archive(
                "output_img",
                "zip",
                os.path.join(os.path.dirname(__file__), "output"),
            )
            ui.notify(f"Done", type="positive")
            remove_all_files("img")
            # timestamp.delete( )
        else:
            print(f"The folder {folder_path} does not exist.")

    ui.button(
        "Download Result",
        on_click=lambda: ui.download(
            os.path.join(os.path.dirname(__file__), "output_img.zip"),
        ),
    )


# apply_imgAug_to_all_images_in_folder('img')
def show_images():
    output_folder = os.path.join(os.path.dirname(__file__), "output")
    images = [
        os.path.join(output_folder, f)
        for f in os.listdir(output_folder)
        if f.endswith(".jpg")
    ]
    with ui.grid(columns=10) as grid:
        for image in images:
            ui.image(image).classes("w-20")
    # return gallery


ui.button("Show Images", on_click=show_images, color="green")
ui.run()
