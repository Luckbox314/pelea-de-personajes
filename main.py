from heroApi import HeroAPI
import random
from miscellaneous import get_team_aligment
import sys
from mailer import send_email
# hero api range from id 1 to 732

# write prints to file
orig_stdout = sys.stdout
f = open('out.txt', 'w+')
sys.stdout = f

# connection to hero api
heroApi = HeroAPI()

ids = [c for c in range(1, 733)]
random.shuffle(ids)
team1 = []
print("Forming team 1.")
i = 0
while len(team1) < 5:
    try:
        print(f"\tAdding hero {ids[i]}.")
        team1.append(heroApi.getHero(ids[i]))
    except:
        print(f"\tError, hero {ids[i]} is missing stats. Trying again with another hero.")
    i += 1
    
print("Forming team 2.")
team2 = []
while len(team2) < 5:
    try:
        print(f"\tAdding hero {ids[i]}.")
        team2.append(heroApi.getHero(ids[i]))
    except:
        print(f"\tError, hero {ids[i]} is missing stats. Trying again with another hero.")
    i += 1

print("Teams formed.")
print(f"\tTeam 1: {team1}")
print(f"\tTeam 2: {team2}")

print("Applying Filiation Coefficient to each hero.")
team1_aligment = get_team_aligment(team1)
print(f"\tTeam 1 aligment: {team1_aligment}")
team2_aligment = get_team_aligment(team2)
print(f"\tTeam 2 aligment: {team2_aligment}")
for hero in team1:
    if hero.aligment == team1_aligment:
        hero.FB = 1 + random.randint(0, 9)
    else:
        hero.FB = 1/(1 + random.randint(0, 9))
        
for hero in team2:
    if hero.aligment == team2_aligment:
        hero.FB = 1 + random.randint(0, 9)
    else:
        hero.FB = 1/(1 + random.randint(0, 9))
    
print("Starting fight.")
i = 1
team1_backup = team1.copy()
team2_backup = team2.copy()
while len(team1) > 0 and len(team2) > 0:
    print(f"\tRound {i}")
    hero1 = team1[0]
    hero2 = team2[0]
    print(f"\t{hero1.name} (Team 1) vs {hero2.name} (Team 2)")
    hero1.reset_hp()
    hero2.reset_hp()
    while hero1.hp > 0 and hero2.hp > 0:
        first = random.randint(1, 2)
        if first == 1:
            hero1.attack(hero2)
            if hero2.hp > 0:
                hero2.attack(hero1)
        else:
            hero2.attack(hero1)
            if hero1.hp > 0:
                hero1.attack(hero2)
        print(f"\t\t{hero1.name} HP: {round(hero1.hp, 2)}")
        print(f"\t\t{hero2.name} HP: {round(hero2.hp, 2)}")
    if hero1.hp > 0:
        team2.pop(0)
        print(f"\t\t{hero1.name} (Team 1) wins the round!")
    else:
        team1.pop(0)
        print(f"\t\t{hero2.name} (Team 2) wins the round!")
    print(f"\t\tRemaining heroes in team 1: {team1}")
    print(f"\t\tRemaining heroes in team 2: {team2}")
    i += 1

print()
print("-----------------------------------------------------")
if len(team1) > 0:
    print(f"Team 1 wins the fight!!")
    print(team1_backup)
else:
    print(f"Team 2 wins the fight!!")
    print(team2_backup)
print("-----------------------------------------------------")


sys.stdout = orig_stdout
f.seek(0)
content = "".join(f.readlines())
print(content)
send_email(sys.argv[1], content)
f.close()