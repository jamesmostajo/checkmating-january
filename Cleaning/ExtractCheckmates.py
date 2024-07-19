import csv

filepath = "Cleaning/info_data.csv"
fileout = "Cleaning/MateElo.csv"

def getMatingPiece(pieceCode):
    pieceName = {
        "Q" : "Queen",
        "R" : "Rook",
        "B" : "Bishop",
        "N" : "Knight",
        "K" : "King",
        "O" : "King"
    }
    if pieceCode.islower():
        return "Pawn"
    return pieceName[pieceCode]

def getSquare(moveNotation, color):
    if "O" in moveNotation:
        side = "1" if color == "White" else "8"
        if len(moveNotation) == 6:
            return "c"+side
        elif len(moveNotation) == 4:
            return "g"+side
    if "=" in moveNotation:
        return moveNotation[-5:-3]
    
    return moveNotation[-3:-1]

with open(filepath, "r") as csvfile:
    with open(fileout, "w") as o:
        csvreader = csv.reader(csvfile)        
        for row in csvreader:
            game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening = row
            if lastMove[-1] == "#":
                score = result.split("-")
                won = "White" if score[0]=="1" else "Black"
                matingPiece = getMatingPiece(lastMove[0])
                square = getSquare(lastMove, won)
                print(*[game_id, lastMove, matingPiece, square,  won, whiteElo, blackElo], sep=',',file=o)
