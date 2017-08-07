import requests
import shutil

CSV_RELEASE_URL = 'https://github.com/joaoevangelista/gwent/releases/download/initial_data/cards.csv'

def main():
    r = requests.get(CSV_RELEASE_URL, stream=True)
    with open('./data/raw/cards.csv', 'w') as f:
        r.raw.decode_content = True
        f.write(str(r.text.encode('utf-8')))

if __name__ == '__main__':
    main()
