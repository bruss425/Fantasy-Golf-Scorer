import requests
import config

"""
ID by tournament (put the tourney id here to make proccessing easier)

2023: 
Players Championship  = 496
St. Jude = 521
"""

tournament_id = "521"


url = "https://golf-leaderboard-data.p.rapidapi.com/leaderboard/" + tournament_id

## do the git ignore config.py things later 
headers = {
	"X-RapidAPI-Key": config.API_KEY,
	"X-RapidAPI-Host": "golf-leaderboard-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

#array of players 
picks = ["Xander Schauffele", "Max Homa", "Wyndham Clark", "Seamus Power"]

players_total = response['results']['tournament']['live_details']['players']
cut_number = response['results']['tournament']['live_details']['cut_value']



## create an array with the positions values of each of the players 
def get_positions(arr):
    positions_array = [None] * 4
    x = 0
    for i in range(players_total):
       for k in range(4):
           name = picks[k].split()
           pick_first = name[0]
           pick_last = name[1]

           player_first = response['results']['leaderboard'][i]['first_name']
           player_last = response['results']['leaderboard'][i]['last_name']
           player_position = response['results']['leaderboard'][i]['position']

           if((pick_first == player_first) and (pick_last == player_last)):
               positions_array[x] = player_position
               x += 1
    
    return positions_array

## arrary to put into the calculate points 

def calulate_points():
    placement = get_positions(picks)
    sum = 0
    for i in range(4): 
        if(placement[i] > cut_number):
            sum -= 3
        elif(placement[i] == 1):
            sum += 12
        elif(placement[i] == 2):
            sum += 9
        elif(placement[i] == 3):
            sum += 8
        elif(placement[i] == 4):
            sum += 7
        elif(placement[i] == 5):
            sum += 6
        elif(placement[i] < 11):
            sum += 5
        elif(placement[i] < 16):
            sum += 4
        elif(placement[i] < 21):
            sum += 3
        elif(placement[i] < 26):
            sum += 2
        else: sum += 1
    
    return sum

points_scored = calulate_points()
print(points_scored)

"""
figure out how to pull data from the rows of players in the sheets 
then put each of of the four names into assigned arrays 
    honeslty i think i could just call them array 1 thru 7 
    I would have to have the row numbers set and i coukd just change them every week 
then calcularte the points for each of the 7 arrays ---> Loop? 
rank the points by name of arrays --> Loop 
then turn those names into real player names like array_2 = Ben 
and present a scoring ranking such as 
1) Ben: 19 points
2) Johns: 23 points 

for special items such as 1.5x tourneys i can either write a function or manually do it
"""







