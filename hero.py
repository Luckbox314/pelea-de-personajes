from random import randint
import math

class Hero:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.power_stats = PowerStats(data['powerstats'])
        self.aligment = data['biography']['alignment']
        self.FB = None
        self.reset_hp()

    def attack(self, hero):
        attack_type = randint(1, 3)
        damage = 0
        if attack_type == 1:
            damage = self.strong_attack(hero)
        elif attack_type == 2:
            damage =  self.fast_attack(hero)
        else:
            damage =  self.mental_attack(hero)
        print(f"\t\t{self.name} inflics {round(damage, 2)} to {hero.name}.")
        
    def mental_attack(self, hero):
        print(f"\t\t{self.name} uses mental attack against {hero.name}.")
        damage = (
            self.power_stats.get_real_stat("intelligence", self.FB) * 0.7 +
            self.power_stats.get_real_stat("speed", self.FB) * 0.2 +
            self.power_stats.get_real_stat("combat", self.FB) * 0.1
        ) * self.FB
        hero.hp -= damage
        return damage
    
    def strong_attack(self, hero):
        print(f"\t\t{self.name} uses strong attack against {hero.name}.")
        damage = (
            self.power_stats.get_real_stat("strength", self.FB) * 0.6 +
            self.power_stats.get_real_stat("power", self.FB) * 0.2 +
            self.power_stats.get_real_stat("combat", self.FB) * 0.2
        ) * self.FB
        hero.hp -= damage
        return damage

    def fast_attack(self, hero):
        print(f"\t\t{self.name} uses fast attack against {hero.name}.")
        damage = (
            self.power_stats.get_real_stat("speed", self.FB) * 0.55 +
            self.power_stats.get_real_stat("durability", self.FB) * 0.25 +
            self.power_stats.get_real_stat("strength", self.FB) * 0.2
        ) * self.FB
        hero.hp -= damage
        return damage

    def reset_hp(self):
        self.hp = math.floor(
            (
                self.power_stats.strength["stat"] * 0.8 + 
                self.power_stats.durability["stat"] * 0.7 + 
                self.power_stats.power["stat"]
            ) / 2 * (1 + self.power_stats.power["AS"]/ 10)
        ) + 100

    def set_FB(self, FB):
        self.FB = FB

    def __str__(self):
        return "Name: " + self.name + "\nAlignment: " + self.aligment + "\nPower Stats: " + str(self.power_stats)
    
    def __repr__(self):
        return self.name 
        




class PowerStats:
    def __init__(self, data):
        self.intelligence = {"stat": int(data["intelligence"]), "AS": randint(0, 10)}
        self.strength = {"stat": int(data["strength"]), "AS": randint(0, 10)} 
        self.speed = {"stat": int(data["speed"]), "AS": randint(0, 10)} 
        self.durability = {"stat": int(data["durability"]), "AS": randint(0, 10)} 
        self.power = {"stat": int(data["power"]), "AS": randint(0, 10)} 
        self.combat = {"stat": int(data["combat"]), "AS": randint(0, 10)} 
        
    def get_real_stat(self, stat, FB):
        powerStat = getattr(self, stat, "Could not find stat")
        return math.floor(((2 * powerStat["stat"] + powerStat["AS"])/1.1) * FB)

    def __str__(self):
        return "Intelligence: " + str(self.intelligence["stat"]) + " (AS: " + str(self.intelligence["AS"]) + ")" + "\n" + \
               "Strength: " + str(self.strength["stat"]) + " (AS: " + str(self.strength["AS"]) + ")" + "\n" + \
               "Speed: " + str(self.speed["stat"]) + " (AS: " + str(self.speed["AS"]) + ")" + "\n" + \
               "Durability: " + str(self.durability["stat"]) + " (AS: " + str(self.durability["AS"]) + ")" + "\n" + \
               "Power: " + str(self.power["stat"]) + " (AS: " + str(self.power["AS"]) + ")" + "\n" + \
               "Combat: " + str(self.combat["stat"]) + " (AS: " + str(self.combat["AS"]) + ")" + "\n"

    def __repr__(self):
        return str(self.intelligence["stat"]) + " "+ str(self.intelligence["AS"]) + "|" + \
               str(self.strength["stat"]) + " "+ str(self.strength["AS"]) + "|" + \
               str(self.speed["stat"]) + " "+ str(self.speed["AS"]) + "|" + \
               str(self.durability["stat"]) + " "+ str(self.durability["AS"]) + "|" + \
               str(self.power["stat"]) + " "+ str(self.power["AS"]) + "|" + \
               str(self.combat["stat"]) + " "+ str(self.combat["AS"])