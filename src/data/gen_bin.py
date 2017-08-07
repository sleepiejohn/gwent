import requests
import csv

from tqdm import tqdm

TOTAL_CARDS = 305  # current amount of cards
CARDS_ENDPOINT = 'https://api.gwentapi.com/v0/cards?limit={0}&offset=0'.format(TOTAL_CARDS)
HEAD = [
    'category',
    'faction',
    'flavor',
    'info',
    'position 1',
    'position 2',
    'position 3',
    'name',
    'group',
    'strength'
]

def get_card_links():
    cards_request = requests.get(CARDS_ENDPOINT)
    resp = cards_request.json()
    return resp['results']


def get_card(link_obj):
    url = link_obj['href']
    card_res = requests.get(url)
    return card_res.json()


def build_card_info(card):
    return {
        'category': safe_access(card['category'], 0, 'name') if 'category' in card else None,
        'faction': card['faction']['name'],
        'flavor': card['flavor'].rstrip(),
        'info': card['info'].rstrip(),
        'position 1': safe_access(card['positions'], 0),
        'position 2': safe_access(card['positions'], 1),
        'position 3': safe_access(card['positions'], 2),
        'name': card['name'],
        'group': card['group']['name'],
        'strength': card['strength'] if 'strength' in card else None
    }


def safe_access(iterable, pos, obj_name):
    return iterable[pos][obj_name] if len(iterable) >= pos + 1 else None


def safe_access(iterable, pos):
    return iterable[pos] if len(iterable) >= pos + 1 else None


def start_writer(file):
    writer = csv.DictWriter(file, HEAD)  # get first set keys since it is all equals
    writer.writeheader()
    return writer

def main():
    links = get_card_links()
    with open('./data/exportable/cards.csv', 'w', newline='', encoding='utf-8') as f:
        writer = start_writer(f)
        for link_obj in tqdm(links):
            card = get_card(link_obj)
            card_dict = build_card_info(card)
            writer.writerow(card_dict)


if __name__ == '__main__':
    main()
