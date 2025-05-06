"""
main.py - основной сценарий запуска парсера.
"""
from parser.loader import load_data_from_excel
from parser.config import RAW_FILE
from parser.inspector import inspect


def parse():
    """Основной сценарий запуска парсера."""

    table = load_data_from_excel(RAW_FILE, 'РЕГЛАМЕНТ', 3, 2, 32)
    inspect(table, 5)


if __name__ == '__main__':
    parse()
