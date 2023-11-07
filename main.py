from nicegui import events, ui
from nicegui.events import ValueChangeEventArguments


def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f"{name}: {event.value}")


with ui.dialog().props("full-width") as dialog:
    with ui.card():
        content = ui.image()


def handle_upload(e: events.UploadEventArguments):
    content.set_content(e.content, format=e.type)
    dialog.open()


with ui.row():
    ui.checkbox("", on_change=show)
    ui.checkbox("Checkbox", on_change=show)
    ui.checkbox("Checkbox", on_change=show)
    ui.checkbox("Checkbox", on_change=show)

ui.upload(on_upload=handle_upload).props("accept=image/*").classes("max-w-full")

ui.run()
