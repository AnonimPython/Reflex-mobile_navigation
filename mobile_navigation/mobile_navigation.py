import reflex as rx
from rxconfig import config


def index() -> rx.Component:
    return rx.container(
        
    )


app = rx.App()
app.add_page(index)
