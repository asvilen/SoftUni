def team_lineup(*args):
    teams_dict = {}
    for player, team in args:
        if team not in teams_dict:
            teams_dict[team] = []
        teams_dict[team].append(player)
    result = ""
    for team, players in sorted(teams_dict.items(), key=lambda item: (-len(item[1]), (item[0]))):
        result += team + ":\n" + "  -" + "\n  -".join(players) + "\n"
    return result


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))


