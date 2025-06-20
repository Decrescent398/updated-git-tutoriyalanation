import reflex as rx
from rxconfig import config

class State(rx.State):

    sidebar_status: bool = True
    page_on: int = 0
    pages: list[str] = ["/", "/ggb",
                "/ig",
                "Setting Up Your Git Identity",
                "Creating Your First GitHub Repository",
                "Connecting Your Local Project to GitHub",
                "Making Changes and Saving them",
                "Creating and Working with Branches ",
                "Merging Changes",
                "Uploading (Pushing) Changes to Github",
                "Forking Repositories",
                "Cloning Repositories",
                "Pull Requests"]

    def toggle_sidebar(self):
        self.sidebar_status = not self.sidebar_status

    @rx.var
    def sync_page(self) -> str:
        try:
            self.page_on = self.pages.index(self.router.page.path)
            return self.router.page.path
        except ValueError:
            self.page_on = 0
            return "/"

    def next_page(self):
        self.page_on = min(self.page_on + 1, len(self.pages) - 1)
        return rx.redirect(self.pages[self.page_on])

    def prev_page(self):
        self.page_on = max(self.page_on - 1, 0)
        return rx.redirect(self.pages[self.page_on])

def nav_controls():
     return rx.flex(
            rx.button("Previous", on_click=State.prev_page),
            rx.button("Next", on_click=State.next_page)
            )

def wrapper(*content: rx.Component):
    return rx.container() #to use in class say index do return wrapper(*index code here)

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.button("-", on_click=State.toggle_sidebar),
        rx.vstack(

            rx.cond(
                State.sidebar_status,
                rx.flex(
                    rx.button("Git & GitHub for Beginners", on_click=rx.redirect("/ggb")),
                    rx.button("Installing Git", on_click=rx.redirect("/ig")),
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
                    direction = "column"
                )
            ),
            
            nav_controls()

        ),
        height = "100vh",
        width = "100vw",
    )

def git_and_github_for_beginners():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.image("/dinos/dino-emergency-meeting.png"),
        ),
        nav_controls(),
        height = "100vh",
        width = "100vw",
    )

def installing_git():
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(),
        nav_controls(),
        height = "100vh",
        width = "100vw"
    )

app = rx.App()

app.add_page(index)
app.add_page(git_and_github_for_beginners, route="/ggb")
app.add_page(installing_git, route="/ig")