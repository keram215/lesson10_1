import random
import requests


def load_random_word():

    url = 'https://jsonkeeper.com/b/LVVW'
    json_data = requests.get(url)
    data = json_data.json()
    random.choice(data)
    word = random.choice(data)
    return word

