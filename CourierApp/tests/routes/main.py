import flet as ft
from flet_model import Router
from Home import Homepage  # go routes.homepage
from SecondPage import Secondp

def main(page: ft.Page):
    page.theme_mode = 'light'

    Router(
        {'home': Homepage(page), 'second_page': Secondp(page)}
    )
    print(page.route)
    page.go(page.route)

ft.app(main)
