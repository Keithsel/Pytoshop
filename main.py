from nicegui import events, ui
from nicegui.events import ValueChangeEventArguments
from Back_End import *
import matplotlib.pyplot as plt
from PIL import Image
import io
import time
import shutil

# import pygetwindow as gw


def clear_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


with ui.row():
    dark = ui.dark_mode()
    ui.label("Switch mode:")
    ui.button("Dark", on_click=dark.enable)
    ui.button("Light", on_click=dark.disable)

with ui.card().classes("w-full items-center"):
    with ui.dialog().props("full-width") as dialog:
        with ui.card():
            content = ui.image()

    def handle_upload(e: events.UploadEventArguments):
        img = Image.open(io.BytesIO(e.content.read()))
        # plt.imshow(img)
        # plt.show()
        img_folder = "img"
        if not os.path.exists(img_folder):
            os.makedirs(img_folder)
        timestamp = int(time.time())
        img_path = os.path.join(img_folder, f"{timestamp}.jpg")
        img.save(img_path)

    clear_folder("img")
    ui.upload(multiple=True, on_upload=handle_upload).props("accept=image/*").classes(
        "max-w-full"
    )

    with ui.column():
        ui.button("Apply Transformations")
        ui.checkbox("apply_geometric_transform", on_change=show)
        slider = ui.slider(min=0, max=100, value=50)
    ui.label().bind_text_from(slider, "value")
    ui.checkbox("color_space_transformations", on_change=show)
    ui.checkbox("kernel_filters", on_change=show)

    def apply_imgAug_to_all_images_in_folder(folder_path):
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".jpg") or filename.endswith(".png"): 
                    image_path = os.path.join(folder_path, filename)
                    img = Image.open(image_path)
                    imgAug(img)
        else:
            print(f"The folder {folder_path} does not exist.")
        
    clear_folder("output")
    apply_imgAug_to_all_images_in_folder("img")

ui.run()
