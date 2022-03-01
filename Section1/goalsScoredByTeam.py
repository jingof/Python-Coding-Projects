"""
Getting goals scored by a team in the
 the 2014/215 premier league season

"""

import urllib.request as rqt
import json

def Solution(teamKey):
    url = "https://s3.eu-west-1.amazonaws.com/hackajob-assets1.p.hackajob/challenges/football_session/football.json"
    response = rqt.urlopen(url)

    # data is a dictionary with name of the season and rounds
    data = json.loads(response.read().decode())
    # we are interested in rounds
    # rounds is a list with a round at every index
    rounds = data.get('rounds')
    teamScore = 0

    for round in rounds: 
        # round is a dictionary with matches 
        # # so we get matches which is a list
        matches = round.get('matches')
        for match in matches:
            # match is a dictionary with the match details
            team1 = match.get('team1')
            team2 = match.get('team2')
            score1 = match.get('score1')
            score2 = match.get('score2')
            if team1.get('key') == teamKey:
                teamScore +=score1
            elif team2.get('key') == teamKey:
                teamScore +=score2
            

    print(data.get('name'))
    return teamScore      
Solution('arsenal')     
""""  
example of match 

match = {'date': '2015-05-24', 
        'team1': {'key': 'arsenal', 'name': 'Arsenal', 'code': 'ARS'}, 
        'team2': {'key': 'westbrom', 'name': 'West Bromwich Albion', 'code': 'WBA'}, 
        'score1': 4, 'score2': 1}
"""
#print(rounds.keys())
