import requests
import json
import random

def get_data():
    r = requests.get("https://jsonkeeper.com/b/LVVW")
    return json.loads(r.text)


def get_word(data):
    random.shuffle(data)
    return data[0]

