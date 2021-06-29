from .get_api import get_all_items
from .characters import CharacterBuilder, Character
from .csv_driver import CsvDriver


ITEMS = [
    'people',
    'planets',
    # 'films',
    # 'species',
    # 'vehicles',
    # 'starships'
]

def fetch_all() -> dict:
    all_items = dict()
    for item in ITEMS:
        all_items[item] = get_all_items(item)
    return all_items

def build_characters() -> list[Character]:
    fetched_data = fetch_all()
    characters = []
    for item in fetched_data['people']:
        characters.append(CharacterBuilder(item, fetched_data['planets']).build())
    return characters

def fetch_to_file() -> str:
    csv = CsvDriver()
    data = build_characters()
    data = [x.to_dict() for x in data]
    return csv.export(data)

if __name__ == '__main__':
    fetch_to_file()
