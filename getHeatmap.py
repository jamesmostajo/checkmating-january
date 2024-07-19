import csv, json
import streamlit as st

filename = "Cleaning/MateElo.csv"
json_filename = "Cleaning/info_data.json"

with open(json_filename, 'r') as json_file:
    games_data = json.load(json_file)

@st.cache_data
def getHeatmapData(pieceFilter, ratingFilter1, ratingFilter2, winnerFilter, tC, op):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        
        data = [[0 for _ in range(8)] for _ in range(8)]
        rows = "87654321"
        columns = "abcdefgh"
        notationToIndex = {}

        # a1 is 00 b1 is 01 c1 is 02
        # a2 is 10 b2 is 11 c2 is 12
        for i in range(8):
            for j in range(8):
                notationToIndex[columns[j]+rows[i]] = (i, j)

        for row in csvreader:
            game_id, mateMove, piece, square, winner, rating1, rating2 = row
            if (pieceFilter != "Select All" and piece != pieceFilter) or (int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2)) or (winnerFilter != "Select Both" and winner != winnerFilter):
                continue
            game_data = games_data.get(game_id)
            timeControl = game_data.get('timeControl')
            opening = game_data.get('opening')
            if (tC == "All" or tC == timeControl) and (op == "All" or op == opening):
                i, j = notationToIndex[square]
                data[i][j] += 1
    
    return data


