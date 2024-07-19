import json

jsonfilename = "Cleaning/EloPieceTakes.json"

def getPieceTakesData(ratingFilter1, ratingFilter2):
    
    with open(jsonfilename, 'r') as jsonfile:
        cumu_elo_takes = json.load(jsonfile)

    ratingFilter1 -= 1

    r1, r2 = str(ratingFilter1), str(ratingFilter2)

    # ['Pawn', 'Rook', 'Knight', 'Bishop', 'Queen', 'King']
    pieces = "PRNBQK"
    takes_in_range = []

    for p in pieces:
        takes_in_range.append(cumu_elo_takes[r2][p] - cumu_elo_takes[r1][p])
    
    return takes_in_range