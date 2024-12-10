import flet as ft
from views.user_main_screen import main_screen
from views.login_screen import login_screen

def main(page: ft.Page):
    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    page.fonts = {
        "TravelingTypewriter": "fonts/TravelingTypewriter.ttf"
    }


    def route_change(route):
        page.views.clear()
        page.views.append(login_screen(page))

        if page.route == "/user_mainscreen":
            page.views.append(main_screen(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
