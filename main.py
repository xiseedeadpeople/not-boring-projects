import flet as ft
from database import init_db, SessionLocal
from services.flight_service import FlightService

from tabs.user_tabs.maintab import main_tab
from tabs.user_tabs.closestflights import closest_flights
from tabs.user_tabs.myorders import my_orders
from tabs.user_tabs.notifstab import notifications
from views.user_mainscr import main_screen
from views.manager_mainscr import manager_mainscreen
from views.login_screen import login_screen


def main(page: ft.Page):
    init_db()
    db = SessionLocal()
    flight_service = FlightService(db)

    page.window.width = 390
    page.window.height = 844
    page.window.always_on_top = True
    page.window.maximizable = False
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0

    def route_change(route):
        page.views.clear()
        page.views.append(login_screen(page))

        if page.route == "/user_mainscreen":
            page.views.append(main_screen(page))

        elif page.route == '/manager_mainscreen':
            page.views.append(manager_mainscreen(page))

        # user tabs
        elif page.route == '/user_mainscreen/main_tab':
            page.views.append(main_tab(page))
        elif page.route == '/user_mainscreen/closest_flights':
            page.views.append(closest_flights(page, flight_service))
        elif page.route == '/user_mainscreen/my_orders':
            page.views.append(my_orders(page))
        elif page.route == '/user_mainscreen/notifications':
            page.views.append(notifications(page))

        # manager tabs

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)
    # page.go("/user_mainscreen")


ft.app(target=main)
