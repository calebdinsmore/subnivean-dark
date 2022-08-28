import xml.etree.ElementTree as et
from PIL import Image

tree = et.parse('Subnivean_Dark.xml')

root = tree.getroot()

pic_urls = []
cards_to_cut = []

for card in root.iter('card'):
    card_name = card.find('name').text
    pic_url = f'https://raw.githubusercontent.com/calebdinsmore/subnivean-dark/main/img/{card_name}.full.jpg'
    pic_urls.append(pic_url)
    # test_response = requests.get(pic_url)
    # if test_response.status_code != 200:
    #     print('FAILED:', pic_url)
    set_el = card.find('set')
    set_el.set('picurl', pic_url)
    related = card.find('related')
    if related is not None:
        related = related.text
        set_el.set('layout', 'transform')
        cards_to_cut.append(related)
        try:
            original = Image.open(f'./img/{card_name}.original.jpg')
        except:
            original = Image.open(f'./img/{card_name}.full.jpg')
            original.save(f'./img/{card_name}.original.jpg')
        front_card = Image.open(f'./img/{card_name}.original.jpg')
        back_card = front_card.copy()
        front_card = front_card.crop((0, 0, 375, 523))
        back_card = back_card.crop((377, 0, 752, 523))
        front_card.save(f'./img/{card_name}.full.jpg')
        back_card.save(f'./img/{related}.full.jpg')

for cut_name in cards_to_cut:
    for card in root.iter('card'):
        if card.find('name').text == cut_name:
            root.find('cards').remove(card)
            print('Cut', cut_name)


tree.write('SND_Processed.xml')




