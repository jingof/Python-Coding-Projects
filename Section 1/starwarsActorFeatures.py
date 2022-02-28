import urllib.request as rqt
import json

def Solution(character):
    chara2 = str(character)
    while " " in chara2:
        chara2 = character.replace(" ", "+")
    url = "https://challenges.hackajob.co/swapi/api/people/?search=" + chara2
    response = rqt.urlopen(url)

    # data is a dictionary with name of the season and rounds
    data = json.loads(response.read().decode())
    results = data.get('results')[0]
    films = results.get('films')
    print(len(films))
    return len(films)
    


Solution("Luke Skywalker")