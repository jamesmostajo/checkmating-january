import csv
import bisect
import streamlit as st
filename = "Cleaning/info_data.csv"

def getHistogramData(tC, op):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        
        eloRanges = [x for x in range(2350, 3050, 50)]
        values = [0 for _ in range(len(eloRanges))]
        
        for game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening in csvreader:
            whiteElo = int(whiteElo); blackElo = int(blackElo)
            gameElo = (whiteElo+blackElo)//2
            if (tC == "All" or tC == timeControl) and (op == "All" or op==opening):
                ind = bisect.bisect(eloRanges, gameElo)
                values[ind] += 1
        
        db = {
            "elo_ranges" : eloRanges,
            "values" : values
        }
    return db




