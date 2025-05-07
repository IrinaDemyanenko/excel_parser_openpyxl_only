"""
type_schemas.py - списки столбцов, сгруппированные по типам данных,
в которые их нужно конвертировать.
"""

# Список колонок, которые нужно привести к int
INT_COLUMNS = [
    'F.H.',
    'LND',
    'MON',
    'Last F.H.',
    'Last LND',
    'Next  F.H.',
    'Next LND',
    'Rem F.H.',
    'Rem LND',
]

# Список колонок, которые нужно привести к datetime
DATETIME_COLUMNS = [
    'Last CAL',
    'Next CAL',
]

# Список колонок, которые нужно привести к строке
STRING_COLUMNS = [
    'Chaprer name',
    'Task number',
    'Item Name',
    'Task Description',
    'Notes',
    'Interval',
    'Data Module Reference',
    'Package',
    'Skill',
    'Effectivity',
    'Revision',
    'Control',
    'Tools',
    'Materials',
    '№ для WPSS',
    'Название для WPSS',
    'Примечания'
]
