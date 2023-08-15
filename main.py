import requests
import config
from sheets import*

"""
ID by tournament (put the tourney id here to make proccessing easier)

2023: 
Players Championship  = 496
St. Jude = 521
BMW Championship : 522
"""

tournament_id = "521"


url = "https://golf-leaderboard-data.p.rapidapi.com/leaderboard/" + tournament_id

## do the git ignore config.py things later 
headers = {
	"X-RapidAPI-Key": config.API_KEY,
	"X-RapidAPI-Host": "golf-leaderboard-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers).json()

\
players_total = response['results']['tournament']['live_details']['players']
cut_number = response['results']['tournament']['live_details']['cut_value']





## create an array with the positions values of each of the players from the array of names
def get_positions(array):
    positions_array = [None] * 4
    x = 0
    for i in range(players_total):
       for k in range(4):
           name = array[k].split()
           pick_first = name[0]
           pick_last = name[1]

           player_first = response['results']['leaderboard'][i]['first_name']
           player_last = response['results']['leaderboard'][i]['last_name']
           player_position = response['results']['leaderboard'][i]['position']

           if((pick_first == player_first) and (pick_last == player_last)):
               positions_array[x] = player_position
               x += 1
    
    return positions_array

## the actual scoring function 
def calulate_points(array):
    placement = get_positions(array)
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
    
    sum = str(sum)
    return sum


print("John's players: ", john_players, "\nPoints: " + calulate_points(john_players))
print("Joe's players: ", joe_players, "\nPoints: " + calulate_points(joe_players))
print("Ben's players: ", ben_players, "\nPoints: " + calulate_points(ben_players))
print("Thomas' players: ", thomas_players, "\nPoints: " + calulate_points(thomas_players))
print("Andrew's players: ", andrew_players, "\nPoints: " + calulate_points(andrew_players))
print("Evan's players: ", evan_players, "\nPoints: " + calulate_points(evan_players))
print("Mike's players: ", mike_players, "\nPoints: " + calulate_points(mike_players))


"""
for special items such as 1.5x tourneys i can either write a function or manually do it
"""







