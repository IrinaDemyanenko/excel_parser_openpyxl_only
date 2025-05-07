"""
cleaner.py - очищает таблицу (list[dict]) от пустых ячеек, прочерков,
переносов строк '\n'.
"""

def strip_strings(x):
    """Удаляет лишние пробелы вначале и в конце строки, если полученное
    значение строка, если не строка - возвращает переданное значение.
    """
    if isinstance(x, str):
        return x.strip()
    return x


def remove_new_lines_n_(x):
    """Удаляет символы переноса строки '\n', если переданное значение строка,
    если не строка - возвращает переданное значение.
    """
    if isinstance(x, str):
        return x.replace('\n', ' ')
    return x


def remove_xa0(x):
    """Удаляет символы неразрывного пробела '\xa0', если переданное значение
    строка, если не строка - возвращает переданное значение.
    """
    if isinstance(x, str):
        return x.replace('\xa0', ' ')
    return x


def check_empty_value(value: str) -> bool:
    """Проверяет, является ли значение в ячейке пустым по смыслу,
    т. е. входит ли в множество {'', ' ', '  ', '   ', '-', '--', '---'},
    если переданное значение строка, если не строка - возвращает False.
    """
    if isinstance(value, str):
        to_check = {'', ' ', '  ', '   ', '-', '--', '---'}
        return value in to_check
    return False


def clean_table(table: list[dict]) -> list[dict]:
    """Очищает таблицу, в виде списка словарей:

    - удаляет лишние пробелы вначале и в конце строки,
    - удаляет символы переноса строки '\n',
    - заменяет пустые по смыслу значения на None.
    """
    cleaned_table = []

    for row in table:
        cleaned_row = {}
        for key, val in row.items():
            val = strip_strings(val)  # очищаем значение от пробелов
            val = remove_new_lines_n_(val)  # от символов переноса
            val = remove_xa0(val)  # от неразрывных пробелов
            if check_empty_value(val):  # заменяем на None
                val = None
            cleaned_row[key] = val
        cleaned_table.append(cleaned_row)  # когда строка готова, добавим в новую таблицу

    return cleaned_table
