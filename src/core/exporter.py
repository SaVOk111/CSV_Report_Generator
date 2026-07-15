"""
Модуль экспорта результатов.
"""

import csv
from datetime import datetime

from core.ascii_chart_builder import ASCIIChartBuilder
from utils.logger import AppLogger


class Exporter:
    """
    Экспортирует сформированный отчет.
    """

    @staticmethod
    def save_csv(report, file_path):
        """
        Сохраняет отчет в CSV.
        """

        if not report:
            raise ValueError(
                "Нет данных для сохранения."
            )

        try:

            with open(
                file_path,
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as file:

                writer = csv.DictWriter(
                    file,
                    fieldnames=report[0].keys()
                )

                writer.writeheader()
                writer.writerows(report)


            AppLogger.info(
                f"CSV экспортирован: {file_path}"
            )


        except PermissionError:

            AppLogger.error(
                f"Нет доступа для записи CSV: {file_path}"
            )

            raise ValueError(
                "Не удалось сохранить CSV.\n"
                "Возможно, файл открыт другой программой."
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка экспорта CSV: {error}"
            )

            raise


    @staticmethod
    def save_txt(report, file_path):
        """
        Сохраняет отчет в текстовый файл.
        """

        if not report:
            raise ValueError(
                "Нет данных для сохранения."
            )


        try:

            horizontal_chart = ASCIIChartBuilder.build(
                report,
                "Горизонтальная"
            )

            percentage_chart = ASCIIChartBuilder.build(
                report,
                "Процентная"
            )


            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:


                file.write("=" * 80 + "\n")
                file.write(
                    " " * 25 +
                    "CSV REPORT GENERATOR\n"
                )
                file.write("=" * 80 + "\n\n")


                file.write(
                    "Дата формирования: "
                    f"{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}\n\n"
                )


                file.write("=" * 80 + "\n")
                file.write("РЕЗУЛЬТАТЫ АНАЛИЗА\n")
                file.write("=" * 80 + "\n\n")


                file.write(
                    f"{'Группа':<24}"
                    f"{'Кол-во':>10}"
                    f"{'Сумма':>12}"
                    f"{'Среднее':>12}"
                    f"{'Медиана':>12}"
                    f"{'Мин':>12}"
                    f"{'Макс':>12}\n"
                )


                file.write("-" * 80 + "\n")


                for row in report:

                    name = str(row["Группа"])

                    if len(name) > 24:
                        name = name[:21] + "..."


                    file.write(
                        f"{name:<24}"
                        f"{row['Количество']:>10}"
                        f"{row['Сумма']:>12.2f}"
                        f"{row['Среднее']:>12.2f}"
                        f"{row['Медиана']:>12.2f}"
                        f"{row['Минимум']:>12.2f}"
                        f"{row['Максимум']:>12.2f}\n"
                    )


                file.write("\n")


                file.write("=" * 80 + "\n")
                file.write(
                    "ГОРИЗОНТАЛЬНАЯ ASCII-ДИАГРАММА\n"
                )
                file.write("=" * 80 + "\n\n")

                file.write(horizontal_chart)


                file.write("\n\n")


                file.write("=" * 80 + "\n")
                file.write(
                    "ПРОЦЕНТНАЯ ASCII-ДИАГРАММА\n"
                )
                file.write("=" * 80 + "\n\n")

                file.write(percentage_chart)


                file.write("\n\n")
                file.write("=" * 80 + "\n")
                file.write(
                    "Конец отчета.\n"
                )


            AppLogger.info(
                f"TXT экспортирован: {file_path}"
            )


        except PermissionError:

            AppLogger.error(
                f"Нет доступа для записи TXT: {file_path}"
            )

            raise ValueError(
                "Не удалось сохранить TXT.\n"
                "Возможно, файл открыт другой программой."
            )


        except Exception as error:

            AppLogger.error(
                f"Ошибка экспорта TXT: {error}"
            )

            raise