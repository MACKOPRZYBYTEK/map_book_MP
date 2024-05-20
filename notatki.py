import json
import requests
from bs4 import BeautifulSoup
users: list[dict] = [
    {"name": "Maciej", "surname": "Przybytek", "posts": 20},
    {"name": "Jan", "surname": "Mielec", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 60},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
    {"name": "Paweł", "surname": "Paszkowski", "posts": 1},
]


miasto=input("Podaj nazwę miejscowości ")
def get_coords(miasto:str) -> list:
    adres_URL=f'https://pl.wikipedia.org/wiki/{miasto}'
    response = requests.get(adres_URL)
    response_HTML=BeautifulSoup(response.text,'html.parser')
    # print(response_HTML)
    latitude=float(response_HTML.select('.latitude')[1].text.replace(',','.'))
    longitude=float(response_HTML.select('.longitude')[1].text.replace(',','.'))
    print([latitude,longitude])
    return latitude,longitude
get_coords(miasto)
