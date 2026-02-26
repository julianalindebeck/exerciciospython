from requests import get

BASE_URL = "https://cdn.nba.com"
ALL_JSON = "/static/json/liveData/scoreboard/todaysScoreboard_00.json"

def get_links():
    resposta = get(BASE_URL + ALL_JSON).json()
    return resposta

def get_games():
    resposta = get_links()
    scoreboard = resposta["scoreboard"]
    games = scoreboard["games"]

    for game in games:
        home_team = game["homeTeam"]
        away_team = game["awayTeam"]
        clock = game["gameClock"]
        period = game["period"]

        """
        print('##############\n')
        print(f'{home_team["teamTricode"]} vs {away_team["teamTricode"]}')
        print(f'{home_team["score"]} x {away_team["score"]}')
        print(f'{clock} - {period}\n')
        """

    return games

def get_home_leaders():
    games = get_games()

    for game in games:
        game_leaders = game["gameLeaders"]
        home_leaders = [game_leaders["homeLeaders"]]
        home_leaders = list(filter(lambda x: x["position"] == "C", home_leaders)) 
        home_leaders.sort(key = lambda x: x["points"])
        print(f'\n{home_leaders}') # imprime listas vazias

get_home_leaders()
