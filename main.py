"""
main.py - основной сценарий запуска парсера.
"""
from parser.loader import load_data_from_excel
from parser.config import CLEANED_FILE
from parser.inspector import inspect
from parser.cleaner import clean_table
from parser.type_schemas import INT_COLUMNS, STRING_COLUMNS, DATETIME_COLUMNS
from parser.convertor import (
    convert_int_col_to_string,
    divide_mixed_col_float_str,
    convert_column_to_int,
    convert_column_to_string
)


def parse():
    """Основной сценарий запуска парсера."""

    table = load_data_from_excel(CLEANED_FILE, 'РЕГЛАМЕНТ', 3, 2, 32)  # загружаем таблицу

    inspect(table, 5)  # смотрим, что загрузили

    table = clean_table(table)  # очищаем от пробелов, переносов, пропусков

    inspect(table, 10)  # смотрим, что загрузили

    # преобразуем типы данных
    table = convert_int_col_to_string(table, 'Chptr')
    table = divide_mixed_col_float_str(table, 'Labor', 'na')

    for col in INT_COLUMNS:
        table = convert_column_to_int(table, col)

    for col in STRING_COLUMNS:
        table = convert_column_to_string(table, col)

    inspect(table, 10)  # смотрим, что загрузили

if __name__ == '__main__':
    parse()
