import requests
from hero import Hero

class HeroAPI:
    def __init__(self):
        self.url = 'https://www.superheroapi.com/api.php/5281794541934977/'

    def getHero(self, id):
        response = requests.get(self.url + str(id))
        data = response.json()
        hero = Hero(data)
        return hero