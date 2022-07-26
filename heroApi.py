import requests
from decouple import config
from hero import Hero

class HeroAPI:
    def __init__(self):
        self.url = 'https://www.superheroapi.com/api.php/'+ config("HERO_API_KEY") + '/'

    def getHero(self, id):
        response = requests.get(self.url + str(id))
        data = response.json()
        hero = Hero(data)
        return hero