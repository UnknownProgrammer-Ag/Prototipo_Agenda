from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Placeholder


class Header(Placeholder):
    DEFAULT_CSS = """
        Header {
            background: #333;
            color: white;
            padding: 1;
            height: 3;
            dock: top;
        }
    """
    pass


class Footer(Placeholder):
    DEFAULT_CSS = """
        Footer {
            background: #333;
            color: white;
            padding: 1;
            height: 3;
            dock: bottom;
        }
    """
    pass


class MainFrame(Screen):
    def compose(self) -> ComposeResult:
        yield Header(id='header')
        yield Footer(id='footer')


class LayoutApp(App):
    def on_mount(self):
        self.push_screen(MainFrame())


if __name__ == '__main__':
    app = LayoutApp()
    app.run()
