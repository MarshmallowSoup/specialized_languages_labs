from .calc_menu import CalcMenu
from .api_menu import APIMenu
from .figures_menu import FiguresMenu
from ..helpers.csv_parse_runner import main
from ..helpers.art_menu import main_menu

class Facade:

    def run_calculator(self):
        calc_menu = CalcMenu()
        calc_menu.run_menu()

    def run_api(self):
        api_menu = APIMenu()
        api_menu.run_menu()

    def run_figures(self):
        figures_menu = FiguresMenu()
        figures_menu.run_menu()

    def run_csv_parse(self):
        main()

    def run_art_menu(self):
        main_menu()