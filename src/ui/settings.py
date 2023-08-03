from supervisely.app.widgets import Text, Card, Button, Container

example_text = Text("This is a widget for settings.", "info")

raise_error_button = Button("Raise error")


@raise_error_button.click
def raise_error():
    raise ValueError("test")


card = Card(
    title="2️⃣ Settings",
    description="PLACEHOLDER: Input description here.",
    content=Container([example_text, raise_error_button]),
    lock_message="Select the dataset on step 1️⃣.",
    collapsable=True,
)
# card.lock()
# card.collapse()
