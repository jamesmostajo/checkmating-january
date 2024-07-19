import csv, json
import streamlit as st
filename = "Cleaning/MateElo.csv"
json_filename = "Cleaning/info_data.json"
with open(json_filename, 'r') as json_file:
    games_data = json.load(json_file)

def getCheckmateData(ratingFilter1, ratingFilter2, tC, op):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        piecesNames = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]
        pieceCheckmateFrequency = [0 for _ in range(6)]

        pieceToIndex = {
            "Pawn" : 0,
            "Knight" : 1,
            "Bishop" : 2,
            "Rook" : 3,
            "Queen" : 4,
            "King" : 5,
        }
        total_checkmates = 0
        for row in csvreader:
            game_id, mateMove, piece, square, winner, rating1, rating2 = row
            if (int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2)):
                continue

            game_data = games_data.get(game_id)
            timeControl = game_data.get('timeControl')
            opening = game_data.get('opening')
            if (tC == "All" or tC == timeControl) and (op == "All" or op == opening):
                pieceCheckmateFrequency[pieceToIndex[piece]] += 1
                total_checkmates += 1

        if  total_checkmates == 0:
            return -1

        data = {
            'piece' : piecesNames,
            'pieceCount' : pieceCheckmateFrequency
        }
    return data




