import reflex as rx

class AppState(rx.State):
    current_section: str = "home"

    def set_section(self, section: str):
        self.current_section = section

def home():
    return rx.box("Bienvenido a la página principal")

def about():
    return rx.box("Acerca de nosotros")

def contact():
    return rx.box("Contáctanos")

def index():
    return rx.vstack(
        rx.hstack(
            rx.button("Home", on_click=lambda: AppState.set_section("home")),
            rx.button("About", on_click=lambda: AppState.set_section("about")),
            rx.button("Contact", on_click=lambda: AppState.set_section("contact")),
        ),
        rx.cond(
            AppState.current_section == "home", home(),
            AppState.current_section == "about", about(),
            AppState.current_section == "contact", contact(),
        )
    )

app = rx.App()
app.add_page(index)
app.compile()
