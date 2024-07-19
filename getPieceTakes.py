import json

jsonfilename = "Cleaning/EloPieceTakes.json"

def getPieceTakesData(ratingFilter1, ratingFilter2, timeControl, openingFilter):
    
    with open(jsonfilename, 'r') as jsonfile:
        cumu_elo_takes = json.load(jsonfile)

    ratingFilter1 -= 1
    r1, r2 = str(ratingFilter1), str(ratingFilter2)

    filename_r1 = "Cleaning/Cumulative/" + str(r1) + ".json"
    filename_r2 = "Cleaning/Cumulative/" + str(r2) + ".json"

    with open(filename_r1, 'r') as jsonfile:
        left_cumu = json.load(jsonfile)
    with open(filename_r2, 'r') as jsonfile:
        right_cumu = json.load(jsonfile)

    # ['Pawn', 'Rook', 'Knight', 'Bishop', 'Queen', 'King']
    pieces = "PRNBQK"
    takes_in_range = []

    for p in pieces:
        takes_in_range.append(right_cumu[timeControl][openingFilter][p] - left_cumu[timeControl][openingFilter][p])
    
    return takes_in_range