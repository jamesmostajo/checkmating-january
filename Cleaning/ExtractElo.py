import csv

elofile = "Cleaning/EloInfo.csv"
game_elo = [] 

rating_freq = [0 for i in range(2299, 3001)]

with open(elofile, 'r') as elof:
    filereader = csv.reader(elof)

    for row in filereader:
        r1, r2 = int(row[1]), int(row[2])
        elo = (r1+r2)//2
        rating_freq[elo - 2299] += 1

cumu_rating_freq = [0 for i in range(2299, 3001)]

for i in range(1, len(rating_freq)):
    cumu_rating_freq[i] = cumu_rating_freq[i-1] + rating_freq[i]

for i in range(len(cumu_rating_freq)):
    print(i+2299, cumu_rating_freq[i], sep=',')

