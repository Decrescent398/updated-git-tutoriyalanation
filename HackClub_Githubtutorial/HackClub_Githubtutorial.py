import reflex as rx
from rxconfig import config

class State(rx.State):
    sidebar_status: bool = True

    def toggle_sidebar(self):
        self.sidebar_status = not self.sidebar_status

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.button("-", on_click=State.toggle_sidebar),
        rx.cond(
            State.sidebar_status,
            rx.vstack(

                rx.button("Git & GitHub for Beginners", on_click=rx.redirect("/ggb")),
                rx.button("Installing Git"),
                rx.button("Setting Up Your Git Identity"),
                rx.button("Creating Your First GitHub Repository"),
                rx.button("Connecting Your Local Project to GitHub"),
                rx.button("Making Changes and Saving them"),
                rx.button("Creating and Working with Branches "),
                rx.button("Merging Changes"),
                rx.button("Uploading (Pushing) Changes to Github"),
                rx.button("Forking Repositories"),
                rx.button("Cloning Repositories"),
                rx.button("Pull Requests"),
            )
        )
    )

def git_and_github_for_beginners():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image("/dinos/dino-emergency-meeting.png"),
        )
    )

app = rx.App()

app.add_page(index)
app.add_page(git_and_github_for_beginners, route="/ggb")