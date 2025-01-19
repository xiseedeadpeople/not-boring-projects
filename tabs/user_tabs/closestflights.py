import flet as ft
from services.flight_service import FlightService
import datetime

def closest_flights(page: ft.Page, flight_service: FlightService):
    # Получение данных о рейсах из базы
    flights_data = flight_service.get_all_flights()

    # Создание карточек рейсов
    flight_cards = []
    for flight in flights_data:
        flight_card = ft.Card(
            content=ft.Container(
                padding=10,
                content=ft.Column(
                    [
                        ft.Row(
                            controls=[ft.Text(f"{flight.from_city} - {flight.to_city}", size=18, weight=ft.FontWeight.BOLD)],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            [
                                ft.Text(f"Дата: {flight.date}", size=18),
                                ft.Text(f"Время вылета: {flight.time}", size=18),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Row(
                            [
                                ft.Text(f"{flight.price}₽", size=18, weight=ft.FontWeight.BOLD, color="green"),
                                ft.ElevatedButton("Бронировать", on_click=lambda e: print(f"Рейс: {flight}")),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    ],
                    spacing=5,
                ),
            ),
        )
        flight_cards.append(flight_card)

    # Добавляем отступ сверху, чтобы карточки не налезали на шапку
    return ft.View(
        route='/user_mainscreen',
        bgcolor='white',
        vertical_alignment=ft.MainAxisAlignment.START,  # Изменено на START для начала с верхней части экрана
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            # Контейнер для карточек с верхним отступом
            ft.Container(
                width=700,
                height=page.window.height, # Высота экрана минус высота шапки (150px)
                padding=ft.Padding(top=150, left=0, right=0, bottom=0),  # Указываем все параметры отступа
                content=ft.Column(
                    flight_cards,
                    scroll=ft.ScrollMode.ADAPTIVE,  # Прокрутка будет активирована, если содержимое выходит за пределы
                ),
            ),
        ],
    )
