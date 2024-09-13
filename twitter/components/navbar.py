import reflex as rx

from twitter.components.form_filed import form_field


def update_user_button() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("user", size=26),
                rx.text("Profile update", size="4", display=[
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
                        "User fields",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Insert new user info",
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
                                "Customer Name",
                                "text",
                                "customer_name", 
                                "user",
                            ),
                            # Location
                            form_field(
                                "Location",
                                "Customer Location",
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
                                "Email", 
                                "user@revision.mail", 
                                "email", 
                                "email", 
                                "mail"
                            ),
                            # Job
                            form_field(
                                "Phone",
                                "User Phone",
                                "text",
                                "phone",
                                "phone"
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
                                rx.button("Submit User"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=None, # on click
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

def navbar():
    return rx.fragment(
            rx.flex(
            update_user_button(),
            rx.spacer(),
            rx.hstack(
                # rx.logo(),
                rx.color_mode.button(),
                align="center",
                spacing="3",
            ),
            spacing="2",
            flex_direction=["column", "column", "row"],
            align="center",
            width="100%",
            top="10px",
        )
    )