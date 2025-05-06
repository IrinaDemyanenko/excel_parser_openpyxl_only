"""
config.py - описание всех путей, используемых в программе
"""
import os


# корень проекта
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# папка с необработанным файлом
RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')

# папка, где будет находиться обработанный файл
JSON_OUT_DIR = os.path.join(BASE_DIR, 'data', 'processed', 'json')

# файл, который нужно спарсить
RAW_FILE = os.path.join(RAW_DIR, 'sample.xlsx')

# файл, созданный после предварительной обработки
CLEANED_FILE = RAW_FILE.replace('.xlsx', '_cleaned.xlsx')

# имя файла после парсинга
JSON_OUT_FILE = os.path.join(JSON_OUT_DIR, 'sample.json')
