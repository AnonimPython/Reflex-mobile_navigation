import reflex as rx
from rxconfig import config

def links(
    icon: str="house",
    text: str="Home",
    href_link: str="#",
    
    ) -> rx.Component:
    return rx.box(
                rx.link(
                    rx.hstack(
                        rx.hstack(
                            rx.box(
                                rx.icon(
                                    tag=icon,
                                    size=30,
                                    background="#e8e9fd",
                                    padding="4px",
                                    border_radius="8px",
                                ),
                                display="flex",
                                align="center",
                                justify="center",
                            ),
                            rx.text(text, weight="bold"),
                            align="center",
                            spacing="2",
                        ),
                        rx.icon(tag="chevron-right"),
                        width="100%",
                        justify="between",
                        align="center",
                    ),
                    href=href_link,
                    color="black",
                    text_decoration="none",
                    _hover={"color": "purple"},
                ),
                margin_top="30px",
            )

def index() -> rx.Component:
    return rx.container(
        rx.box(
            #*person | name | work
            rx.box(
                rx.flex(
                    # person
                    rx.image(
                        "/person.jpg",
                        width="70px",
                        height="70px",
                        border_radius="10px",
                        border="1px solid purple",
                        margin_right="10px",
                    ),
                    rx.vstack(
                        # name
                        rx.text(
                            "Elizabeth Comandore",
                            margin_top="10px",
                            weight="bold",
                            size="5"
                        ),
                        # work
                        rx.text("Environmental meteorologist"),
                    ),
                    align="center",
                    align_start="center",
                ),    
                padding_top="20px"
            ), 
            rx.separator(
                width="100%",
                margin="auto",
                margin_top="20px",
            ),
            #* main links
            links(
                icon="user-round",
                text="Personal Information",
            ),
            links(
                icon="mail",
                text="Massage",
            ),
            links(
                icon="bell",
                text="Notification",
            ),
            links(
                icon="map-pin",
                text="Location",
            ),
            links(
                icon="handshake",
                text="Community",
            ),
            rx.separator(
                width="100%",
                margin="auto",
                margin_top="20px",
            ),
            #* additional links
            links(
                icon="book-open-check",
                text="FAQs",
            ),
            links(
                icon="book-open-check",
                text="FAQs",
            ),
            links(
                icon="settings",
                text="Settings",
            ),
            #* navbar 
            #! (i dont't use position:fixed)
            rx.box(
                rx.hstack(
                    rx.link(
                        rx.icon(tag="home",size=30,),
                        href="#",
                        color="#e9ebf3",
                    ),
                    rx.link(
                        rx.icon(tag="chart-no-axes-combined",size=30,),
                        href="#",
                        color="#e9ebf3",
                    ),
                    rx.link(
                        rx.icon(tag="mail",size=30,),
                        href="#",
                        color="#e9ebf3",
                    ),
                    rx.box(
                        rx.icon(
                            tag="user",
                            size=35,
                            background="#f6f7ff",
                            padding="4px",
                            border_radius="15px",
                        ),
                        display="flex",
                        align="center",
                        justify="center",
                    ),
                    
                    justify="between",
                ),
                
                
                background="#fff",
                margin_top="27%",
            ),
            
            width="400px",
            height="800px",
            background="#fff",
            margin="auto",
            border_radius="30px",
            margin_top="100px",
            padding="20px",
            style={
                "-webkit-box-shadow": "4px 4px 84px 0px rgba(34, 60, 80, 0.3)",
                "-moz-box-shadow": "4px 4px 84px 0px rgba(34, 60, 850, 0.3)",
                "box-shadow": "4px 4px 84px 0px rgba(34, 60, 80, 0.3)",
            }
        ),
        
        
        background="#e9ebf3",
        height="100vh",
        width="100%"
    )


app = rx.App()
app.add_page(index)
