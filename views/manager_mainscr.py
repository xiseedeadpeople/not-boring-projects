import flet as ft
from flet_core import LinearGradient

def manager_mainscreen(page: ft.Page):
    return ft.View(
        route='/manager_mainscreen',
        controls=[
            ft.Column([
                ft.Text('manager'),
                ft.Container(
                    margin=ft.margin.only(top=page.window.height / 2),
                    alignment=ft.alignment.center,
                    content=ft.Column([ft.Text('Manager', size=30, color='black')])
                )
            ])
        ],
        bgcolor='#FFFFFF'
    )
