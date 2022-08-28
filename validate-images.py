import xml.etree.ElementTree as et
import requests

tree = et.parse('Subnivean_Dark.xml')

root = tree.getroot()

for card in root.iter('card'):
    card_name = card.find('name').text
    related = card.find('related')
    pic_url = f'https://raw.githubusercontent.com/calebdinsmore/subnivean-dark/main/img/{card_name}.full.jpg'
    test_response = requests.get(pic_url)
    if test_response.status_code != 200:
        print('FAILED:', pic_url)
    if related:
        related = related.text
        pic_url = f'https://raw.githubusercontent.com/calebdinsmore/subnivean-dark/main/img/{related}.full.jpg'
        test_response = requests.get(pic_url)
        if test_response.status_code != 200:
            print('FAILED:', pic_url)
