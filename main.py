from sanic import Sanic
from sanic.response import json, text
from Model.ChampionsLeagueModel import ChampionsLeagueModel

app = Sanic('Champions League Challenge')

# api path variable
PATH_API = '/api'


# Route home
@app.route("/", methods=['GET'])
async def home(request):
    return text('API REST CHAMPIONS LEAGUE')


# 1. Route about
@app.route(PATH_API + "/champions-league/", methods=['GET'])
async def about(request):
    return json(ChampionsLeagueModel.getAbout())


# 2. Route aboutFinal
@app.route(PATH_API + "/champions-league/<season>", methods=['GET'])
async def aboutFinal(request, season):
    try:
        ret = ChampionsLeagueModel.getAboutBySeason(season=season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 3. Route get all teams
@app.route(PATH_API + "/champions-league/<season>/teams/", methods=['GET'])
async def teams(request, season):
    try:
        ret = ChampionsLeagueModel.getAllTeams(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 4. Route get one tem
@app.route(PATH_API + "/champions-league/<season>/teams/<name>", methods=['GET'])
async def team(request, season, name):
    try:
        ret = ChampionsLeagueModel.getOneTeam(season, name)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 5. Route get all groups
@app.route(PATH_API + "/champions-league/<season>/group-stage/", methods=['GET'])
async def groups(request, season):
    try:
        ret = ChampionsLeagueModel.getGroups(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 6. Route get one group variable name using only one letter between A and H
@app.route(PATH_API + "/champions-league/<season>/group-stage/<name>", methods=['GET'])
async def group(request, season, name):
    try:
        ret = ChampionsLeagueModel.getGroups(season, name)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 7. Route round of 16
@app.route(PATH_API + "/champions-league/<season>/round-of-16/", methods=['GET'])
async def round16(request, season):
    try:
        ret = ChampionsLeagueModel.getRound16(season)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# 11 Route Final
@app.route(PATH_API + "/champions-league/<season>/final/<team1>/vs/<team2>", methods=['GET'])
async def group(request, season, team1, team2):
    try:
        ret = ChampionsLeagueModel.getFinal(season, team1, team2)
    except Exception as e:
        ret = {"error ": str(e)}

    return json(ret)


# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
