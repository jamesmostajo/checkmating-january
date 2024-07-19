import csv, json
from Openings import openings

results = ["Draw", "Checkmate", "Abandoned", "Resigned", "Time Forfeit"]
gameTypes = ["All", "Blitz", "Rapid", "Classical"]

EloTimeResOpenings = {
    elo: {
        gameType: {
            opening: {res: 0 for res in results}
            for opening in openings
        }
        for gameType in gameTypes
    }
    for elo in range(2299, 3001)
}

CumuEloTimeResOpenings = {
    elo: {
        gameType: {
            opening: {res: 0 for res in results}
            for opening in openings
        }
        for gameType in gameTypes
    }
    for elo in range(2299, 3001)
}

filesource = "Cleaning/info_data.csv"
elofile = "Cleaning/EloInfo.csv"
game_elo = [] 

with open(elofile, 'r') as elof:
    filereader = csv.reader(elof)

    for row in filereader:
        r1, r2 = int(row[1]), int(row[2])
        elo = (r1+r2)//2
        game_elo.append(elo)

with open(filesource, 'r') as file:
    filereader = csv.reader(file)

    for row in filereader:
        game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening = row
        game_id = int(game_id)
        score = result.split('-')
        cur_elo = game_elo[game_id]

        if "1/2" in score:
            result_type = "Draw"
        elif '#' in lastMove:
            result_type = "Checkmate"
        elif termination == "Abandoned":
            result_type = "Abandoned"
        elif termination == "Normal":
            result_type = "Resigned"
        elif termination == "Time forfeit":
            result_type = "Time Forfeit"
        else:
            continue

        EloTimeResOpenings[cur_elo][timeControl][opening][result_type] += 1
        EloTimeResOpenings[cur_elo][timeControl]["All"][result_type] += 1
        EloTimeResOpenings[cur_elo]["All"][opening][result_type] += 1
        EloTimeResOpenings[cur_elo]["All"]["All"][result_type] += 1

for elo in range(2301, 3000):
    for gameType in gameTypes:
        for opening in openings:
            for result in results:
                CumuEloTimeResOpenings[elo][gameType][opening][result] = (
                    EloTimeResOpenings[elo][gameType][opening][result] -
                    EloTimeResOpenings[elo-1][gameType][opening][result]
                )


json_file = "Cleaning/EloTimeResultsOpenings.json"
with open(json_file, 'w') as json_file:
    json.dump(CumuEloTimeResOpenings, json_file)