def get(searchSpace, toFind):
    startInd = searchSpace.find(toFind) + len(toFind) + 1
    returnString = ""
    index = startInd
    while searchSpace[index] != "\"":
        returnString += searchSpace[index]
        index += 1
    return returnString

def getLastMove(moves, termination):
    if len(moves) == 0 or termination == "Abandoned":
        return -1
    else:
        return moves[-1]

filename = "Cleaning/lichess_elite_2023-01.pgn"
filepath = "Cleaning/info_data_withmoves.csv"

game_id = 0
f = open(filename, "r")
s = open(filepath,"w")

data = f.read()

data = str(data)
raw_data = data.split("[Event ")

del raw_data[0]

games = []
game_id = 0
print(len(raw_data))
for game_index in range(len(raw_data)):
    game = raw_data[game_index]
    moves = game[game.find("1. "):].split()[:-1]
    whiteElo = get(game, "WhiteElo ")
    blackElo = get(game, "BlackElo ")
    timeControl = get(game, "Rated").split()[0]
    termination = get(game, "Termination ")
    result = get(game, "Result ")
    lastMove = getLastMove(moves, termination)
    opening = '\"' + get(game, "Opening ") + '\"'
    nmoves = ""
    for token in moves:
        if "." in token: continue
        nmoves += token + ";"
    info = [game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening, nmoves[:-1]]
    print(*info, sep=',', file = s)
    game_id+=1

f.close()
s.close()