import csv

filepath = "Cleaning/info_data.csv"
fileout = "Cleaning/Openings.csv"

with open(filepath, "r") as csvfile:
    with open(fileout, "w") as o:
        csvreader = csv.reader(csvfile) 
        openings = set()       
        for row in csvreader:
            game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening = row
            openings.add(opening)
        

        print(*openings, sep=';', file=o)
            