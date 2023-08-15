import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("2023 Fantasy Golf").worksheet('Tournaments')


## the row for the tournmanet of the week
row = 83 ## 83 = St. Jude 

## settings which set of players are which 
john_row = row + 1
joe_row = row + 2
ben_row = row + 3
thomas_row = row + 4
andrew_row = row + 5
evan_row = row + 6
mike_row = row + 7

## making arrays of players for each person in leauge
def make_array(person_row):
    players_array = [None] * 4
    for i in range(4):
        players_array[i] = sheet.cell(person_row, i + 2).value
    
    return players_array

## everyones personal arrays 
john_players = make_array(john_row)
joe_players = make_array(joe_row)
ben_players = make_array(ben_row)
thomas_players = make_array(thomas_row)
andrew_players = make_array(andrew_row)
evan_players = make_array(evan_row)
mike_players = make_array(mike_row)



    



