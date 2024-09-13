import reflex as rx

from twitter.components.form_filed import form_field
from twitter.state.base import State


def add_marketplace_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("plus", size=26),
                rx.text("Add marketplace", size="4", display=[
                        "none", "none", "block"]),
                size="3",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="users", size=34),
                    color_scheme="blue",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Marketplace fields",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Inser new mp info",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        rx.hstack(
                            # Name
                            form_field(
                                "Name",
                                "Marketplace Name",
                                "text",
                                "marketplace_name", 
                                "user",
                            ),
                            # Location
                            form_field(
                                "Scheme",
                                "fbs, fbo",
                                "text",
                                "location",
                                "map-pinned"
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        rx.hstack(
                            # Email
                            form_field(
                                "Client id", 
                                "client_id", 
                                "text", 
                                "client_id", 
                                "key"
                            ),
                            # Job
                            form_field(
                                "Api key",
                                "api_key",
                                "text",
                                "api_key",
                                "key"
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        # Gender
                        # rx.vstack(
                        #     rx.hstack(
                        #         rx.icon("user-round", size=16, stroke_width=1.5),
                        #         rx.text("Gender"),
                        #         align="center",
                        #         spacing="2",
                        #     ),
                        #     rx.select(
                        #         ["Male", "Female", "Other"],
                        #         placeholder="Select Gender",
                        #         name="gender",
                        #         direction="row",
                        #         as_child=True,
                        #         required=True,
                        #         width="100%",
                        #     ),
                        #     width="100%",
                        # ),
                        # rx.hstack(
                        #     # Age
                        #     form_field(
                        #         "Age",
                        #         "Customer Age",
                        #         "number",
                        #         "age",
                        #         "person-standing",
                        #     ),
                        #     # Salary
                        #     form_field(
                        #         "Salary",
                        #         "Customer Salary",
                        #         "number",
                        #         "salary",
                        #         "dollar-sign"
                        #     ),
                        #     spacing="3",
                        #     width="100%",
                        # ),
                        width="100%",
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Submit Marketplace"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=State.add_marketplace, # on click
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            style={"max_width": 450},
            box_shadow="lg",
            padding="1.5em",
            border=f"2.5px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )