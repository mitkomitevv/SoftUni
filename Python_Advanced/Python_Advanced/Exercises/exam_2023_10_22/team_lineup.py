def team_lineup(*args):
    teams = {}

    for player, country in args:
        if country not in teams:
            teams[country] = []
        teams[country].append(player)

    sorted_teams = dict(sorted(teams.items(), key=lambda x: (-len(x[1]), x[0])))

    # result = []
    # for country, players in sorted_teams.items():
    #     team_list = f"{country}:\n  -" + "\n  -".join(players)
    #     result.append(team_list)
    #
    # return '\n'.join(result)

    return '\n'.join([f"{country}:\n  -" + "\n  -".join(players) for country, players in sorted_teams.items()])

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
