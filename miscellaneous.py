
def get_team_aligment(team):
    good = 0
    for hero in team:
        if hero.aligment == "good":
            good += 1
    if good > len(team) / 2:
        return "good"
    else:
        return "bad"
