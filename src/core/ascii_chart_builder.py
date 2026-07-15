"""
Модуль построения ASCII-диаграмм.
"""


class ASCIIChartBuilder:
    """
    Построение ASCII-диаграмм по данным отчета.
    """

    BAR_SYMBOL = "#"

    NAME_WIDTH = 24
    BAR_WIDTH = 35

    @staticmethod
    def build(report, chart_type):
        """
        Построить ASCII-диаграмму.

        Parameters
        ----------
        report : list[dict]
        chart_type : str

        Returns
        -------
        str
        """

        if not report:
            return "Нет данных для построения диаграммы."

        if chart_type == "Горизонтальная":
            return ASCIIChartBuilder._build_horizontal(report)

        if chart_type == "Процентная":
            return ASCIIChartBuilder._build_percentage(report)

        return "Неизвестный тип диаграммы."

    # ==========================================================
    # Горизонтальная диаграмма
    # ==========================================================

    @staticmethod
    def _build_horizontal(report):

        max_value = max(row["Сумма"] for row in report)

        scale = (
            ASCIIChartBuilder.BAR_WIDTH / max_value
            if max_value > 0
            else 1
        )

        lines = []

        lines.append("=" * 80)
        lines.append(" " * 25 + "ASCII REPORT CHART")
        lines.append("=" * 80)
        lines.append("")
        lines.append("Тип диаграммы      : Горизонтальная")
        lines.append(f"Количество групп   : {len(report)}")
        lines.append(f"Максимум           : {max_value:.2f}")
        lines.append("")
        lines.append("-" * 80)
        lines.append(
            f"{'Категория':<{ASCIIChartBuilder.NAME_WIDTH}} "
            f"{'Диаграмма':<{ASCIIChartBuilder.BAR_WIDTH}} "
            f"{'Значение':>10}"
        )
        lines.append("-" * 80)

        total = 0
        minimum = max_value

        for row in report:

            name = str(row["Группа"])

            if len(name) > ASCIIChartBuilder.NAME_WIDTH:
                name = (
                    name[:ASCIIChartBuilder.NAME_WIDTH - 3]
                    + "..."
                )

            value = float(row["Сумма"])

            total += value
            minimum = min(minimum, value)

            length = int(value * scale)

            if value > 0:
                length = max(1, length)

            bar = ASCIIChartBuilder.BAR_SYMBOL * length

            lines.append(
                f"{name:<{ASCIIChartBuilder.NAME_WIDTH}} "
                f"{bar:<{ASCIIChartBuilder.BAR_WIDTH}} "
                f"{value:>10.2f}"
            )

        lines.append("-" * 80)
        lines.append(f"Минимум            : {minimum:.2f}")
        lines.append(f"Сумма              : {total:.2f}")
        lines.append(
            f"1 символ ≈ {max_value / ASCIIChartBuilder.BAR_WIDTH:.2f}"
        )
        lines.append("=" * 80)

        return "\n".join(lines)

    # ==========================================================
    # Процентная диаграмма
    # ==========================================================

    @staticmethod
    def _build_percentage(report):

        total = sum(row["Сумма"] for row in report)

        lines = []

        lines.append("=" * 80)
        lines.append(" " * 20 + "ASCII PERCENTAGE CHART")
        lines.append("=" * 80)
        lines.append("")
        lines.append("Тип диаграммы      : Процентная")
        lines.append(f"Количество групп   : {len(report)}")
        lines.append(f"Общая сумма        : {total:.2f}")
        lines.append("")
        lines.append("-" * 80)

        lines.append(
            f"{'Категория':<{ASCIIChartBuilder.NAME_WIDTH}} "
            f"{'Диаграмма':<{ASCIIChartBuilder.BAR_WIDTH}} "
            f"{'Доля':>10}"
        )

        lines.append("-" * 80)

        percent_sum = 0

        for row in report:

            name = str(row["Группа"])

            if len(name) > ASCIIChartBuilder.NAME_WIDTH:
                name = (
                    name[:ASCIIChartBuilder.NAME_WIDTH - 3]
                    + "..."
                )

            value = float(row["Сумма"])

            percent = (
                value / total * 100
                if total > 0
                else 0
            )

            percent_sum += percent

            length = int(
                percent / 100
                * ASCIIChartBuilder.BAR_WIDTH
            )

            if percent > 0:
                length = max(1, length)

            bar = ASCIIChartBuilder.BAR_SYMBOL * length

            lines.append(
                f"{name:<{ASCIIChartBuilder.NAME_WIDTH}} "
                f"{bar:<{ASCIIChartBuilder.BAR_WIDTH}} "
                f"{percent:>8.2f}%"
            )

        lines.append("-" * 80)
        lines.append(f"Итого              : {percent_sum:.2f}%")
        lines.append(
            f"1 символ ≈ {100 / ASCIIChartBuilder.BAR_WIDTH:.2f}%"
        )
        lines.append("=" * 80)

        return "\n".join(lines)