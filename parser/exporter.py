"""
exporter.py - сохранение list[dict] в файл JSON.
"""
import os
import json
from parser.config import JSON_OUT_FILE


def export_to_json(table: list[dict], output_path: str = JSON_OUT_FILE):
    """Экспоритрует данные из таблицы в форме списка словарей, сохраняет в .json файл.

    table: таблица в виде list[dict]
    output_path: путь для сохранения файла

    Особенности экспорта:
     - каждая строка будет отдельным объектом словаря;
     - без преобразования кирилицы;
     - даты в виде строк ('ДД.ММ.ГГГГ').
    """
    # защита от ошибки сохранения, если папки нет
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # открываем файл на запись, указываем кодировку UTF-8, чтобы правильно сохранить кириллицу
    with open(output_path, 'w', encoding='utf-8') as out_file:

        json.dump(
            table,  # что
            out_file,  # куда
            ensure_ascii=False, # не экранировать кириллицу
            indent=4  # отступы 4 пробела
        )

    print(f'\nТаблица конвертирована в JSON файл: {output_path}\n')
