"""
Модуль логирования приложения.
"""

from pathlib import Path
import logging


class AppLogger:
    """
    Логгер приложения.
    """

    _initialized = False

    @classmethod
    def initialize(cls):
        """
        Настроить систему логирования.
        """

        if cls._initialized:
            return

        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        logging.basicConfig(
            filename=log_dir / "app.log",
            level=logging.INFO,
            format="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%d.%m.%Y %H:%M:%S",
            encoding="utf-8"
        )

        cls._initialized = True

        cls.info("Программа запущена.")

    @staticmethod
    def info(message):
        """
        Записать информационное сообщение.
        """

        logging.info(message)

    @staticmethod
    def warning(message):
        """
        Записать предупреждение.
        """

        logging.warning(message)

    @staticmethod
    def error(message):
        """
        Записать ошибку.
        """

        logging.error(message)