"""
convertor.py - преобразует значения в колонках к требуемому типу данных.
"""

def convert_int_col_to_string(table: list[dict], col_name: str) -> list[dict]:
    """Преобразует значения в колонке col_name в строку из 2-х символов,
    при необходимости дополнит ведущими нулями.
    7 -> '07'
    12 -> '12'

    table: таблица в виде list[dict]
    col_name: имя колонки, значения в которой нужно конвертировать
    """
    for row in table:
        value = row.get(col_name)
        if isinstance(value, int):  # если в ячейке число
            value = f'{value:02}'
            row[col_name] = value
        elif isinstance(value, str) and value.isdigit():  # если в ячейке строка из цифр
            value = value.zfill(2)
            row[col_name] = value

    return table


def divide_mixed_col_float_str(table: list[dict], col_name: str, ending: str) -> list[dict]:
    """Делит колонку со смешанными значениями на две:

    - в одной колонке col_name останутся значения float,
    - во втрой колонке col_name_ending отстанутся строки.

    table: таблица в виде list[dict],
    col_name: имя колонки, которую нужно разделить на две,
    ending: окончание, которое добавить к имени колонки, чтобы сформировать
    новое имя, для колонки со строковыми значениями.
    """
    for row in table:
        value = row.get(col_name)
        try:
            row[col_name] = float(value)  # в исходной колонке оставляем float
            row[f'{col_name}_{ending}'] = None  # в новой запишем None
        except (ValueError, TypeError):         # ValueError — если 'n/a', TypeError — если None
            row[f'{col_name}_{ending}'] = value
            row[col_name] = None

    return table


def convert_column_to_int(table: list[dict], col_name: str) -> list[dict]:
    """Преобразует значение в колонке col_name в int.

    table: таблица в виде list[dict]
    col_name: имя колонки, значения в которой нужно конвертировать.

    Выводит в консоль значения из колонки, которые не удалось конвертировать,
    чтобы предотвратить потерю важных данных.
    """
    failed_values = set()

    for row in table:
        value = row.get(col_name)
        try:
            value = str(value).replace(',', '.')  # если значение считалось как строка '12,0', то станет '12.0'
            row[col_name] = int(float(value))
        except (ValueError, TypeError):
            failed_values.add(value)
            row[col_name] = None

    print(
        f'\nПреобразуем колонки к int\n'
        f'Не удалось конвертировать в int в колонке {col_name} значения:\n'
        f'{failed_values}\n'
        f'\nКонец преобразования колонок к int\n'
        )

    return table


def convert_column_to_string(table: list[dict], col_name: str) -> list[dict]:
    """Преобразует значение в колонке col_name в str.

    table: таблица в виде list[dict]
    col_name: имя колонки, значения в которой нужно конвертировать.

    Выводит в консоль значения, которые не удалось привести к строке,
    чтобы предотвратить потерю важных данных.
    """
    failed_values = set()

    for row in table:
        value = row.get(col_name)
        try:
            row[col_name] = str(value)
        except Exception:  # Exception перехват любого исключения
            failed_values.add(value)
            row[col_name] = None

    print(
        f'\nПреобразуем значения колонок к строкам\n'
        f'Не удалось конвертировать в str в колонке {col_name} значения:\n'
        f'{failed_values}\n'
        f'\nКонец преобразования значений колонок к строкам\n'
        )

    return table
