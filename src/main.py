"""
Точка входа в приложение.

Запускает главное окно программы.
"""

from ui.main_window import MainWindow
from utils.logger import AppLogger


def main():
    """
    Главная функция приложения.
    """
    app = MainWindow()

    AppLogger.initialize()
    
    app.run()


if __name__ == "__main__":
    main()