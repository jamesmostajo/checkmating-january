import csv
import streamlit as st

filename = "Cleaning/SortedElo.csv"

@st.cache_data
def getGamesNum(ratingFilter1, ratingFilter2):

    lower_count, upper_count = 0, 0
    ratingFilter1 -= 1  # for memory saving

    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            ave_rating = int(row[0])
            num_games = int(row[1])
            if ave_rating == ratingFilter1:
                lower_count = num_games
            if ave_rating == ratingFilter2:
                upper_count = num_games
            
                
    return upper_count - lower_count


