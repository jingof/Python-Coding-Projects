import urllib.request as rqt
import json

def Solution(film,character):
    chara2 = str(character)
    while " " in chara2:
        chara2 = character.replace(" ", "+")
    url = "https://challenges.hackajob.co/swapi/api/people/?search=" + chara2
    response = rqt.urlopen(url)

    # data is a dictionary with name of the season and rounds
    data = json.loads(response.read().decode())
    results = data.get("results")
    if len(results) != 0:      
        results = data.get('results')[0]
        movies = results.get('films')
        actorFilms = []
        diction = {}
        for movie in movies:
            response1 = rqt.urlopen(movie)
            data1 = json.loads(response1.read().decode())
            title = data1.get('title')
            diction[title] = data1
            actorFilms.append(title)
        actorFilms.sort()
        actorFilms=", ".join(actorFilms)
    else:
        actorFilms = "none"
        
    filimu = str(film)
    while " " in filimu:
        filimu = film.replace(" ", "+")
    url2 = "https://challenges.hackajob.co/swapi/api/films/?search=" + filimu
    response2 = rqt.urlopen(url2)

    data2 = json.loads(response2.read().decode())
    if len(data2.get("results")) != 0:
        results = data2.get("results")[0]
        actors = results.get("characters")
        characterNames = []
        for actor in actors:
            response1 = rqt.urlopen(actor)
            data1 = json.loads(response1.read().decode())
            characterNames.append(data1.get("name"))
        characterNames.sort()
        characterNames=", ".join(characterNames)
    else:
        characterNames = "none"
    #print(actorFilms)
    #print(characterNames)
    finalString = film+": "+characterNames+"; "+character+": "+actorFilms
    

    print()
    print(finalString)
    return finalString
    


#Solution("","Luke Skywalker")
#Solution("A New Hope","Raymus Antilles")
Solution("The Force Awakens","Walter White")