import csv, json
from Openings import openings

results = ["Draw", "Checkmate", "Abandoned", "Resigned", "Time Forfeit"]
pieceCaptures = list("PRNBQK")
innerDimension = results + pieceCaptures
gameTypes = ["All", "Blitz", "Rapid", "Classical"]

EloTimeResOpenings = {
    elo: {
        gameType: {
            opening: {res: 0 for res in innerDimension}
            for opening in openings
        }
        for gameType in gameTypes
    }
    for elo in range(2299, 3001)
}

CumuEloTimeResOpenings = {
    elo: {
        gameType: {
            opening: {res: 0 for res in innerDimension}
            for opening in openings
        }
        for gameType in gameTypes
    }
    for elo in range(2299, 3001)
}

filesource = "Cleaning/info_data_withmoves.csv"
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
        game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening, movesRaw = row
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
        
        moves = movesRaw.split(';')

        EloTimeResOpenings[cur_elo][timeControl][opening][result_type] += 1
        EloTimeResOpenings[cur_elo][timeControl]["All"][result_type] += 1
        EloTimeResOpenings[cur_elo]["All"][opening][result_type] += 1
        EloTimeResOpenings[cur_elo]["All"]["All"][result_type] += 1

        for move in moves:
            if 'x' in move:
                capturing_piece = move[move.index('x') - 1]
                if capturing_piece not in "RNBQK":
                    capturing_piece = "P"
                
                EloTimeResOpenings[cur_elo][timeControl][opening][capturing_piece] += 1
                EloTimeResOpenings[cur_elo][timeControl]["All"][capturing_piece] += 1
                EloTimeResOpenings[cur_elo]["All"][opening][capturing_piece] += 1
                EloTimeResOpenings[cur_elo]["All"]["All"][capturing_piece] += 1



for elo in range(2300, 3001):
    for gameType in gameTypes:
        for opening in openings:
            for result in innerDimension:
                CumuEloTimeResOpenings[elo][gameType][opening][result] = (
                    EloTimeResOpenings[elo][gameType][opening][result] +
                    CumuEloTimeResOpenings[elo-1][gameType][opening][result]
                )
print("now done preprocessing")
print("will now print to json")

for elo in range(2300, 3001):
    json_file = "Cleaning/Cumulative/"+str(elo)+".json"
    with open(json_file, 'w') as json_file:
        json.dump(CumuEloTimeResOpenings[elo], json_file)