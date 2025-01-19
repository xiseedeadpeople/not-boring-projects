import flet as ft
from services.flight_service import FlightService
import datetime


def notifications(page: ft.Page):
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[ft.Text('Уведомлений нет', color='black', size=30)],
    )
