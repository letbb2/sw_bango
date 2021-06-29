import requests

URL = 'http://swapi.dev/api/'

def get_query(spec: str) -> dict:
    data = requests.get(URL + spec)
    if data.status_code == 200:
        return data.json()
    if data.status_code == 404:
        print(data.url)
        raise Exception('sw api returned 404, very bad indeed')
    raise Exception('unhandled sw api exception')

def get_spec(name: str, page) -> str:
    return f"{name}/{page}"

def get_all_items(item: str) -> list:
    results = []
    next = True
    num = 1
    while (next):
        ans = get_query(get_spec(item, f'?page={num}'))
        next = ans['next']
        results.extend(ans['results'])
        num = num + 1
    return results
