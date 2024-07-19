import json

jsonbase = "Cleaning/Cumulative/"
ext = ".json"
def getPieGameresults(ratingFilter1, ratingFilter2, timeControl, openingFilter):

    ratingFilter1 -= 1
    r1, r2 = str(ratingFilter1), str(ratingFilter2)

    with open(jsonbase+r1+ext, 'r') as jsonfile:
        cumu_elo_res1 = json.load(jsonfile)

    with open(jsonbase+r2+ext, 'r') as jsonfile:
        cumu_elo_res2 = json.load(jsonfile)


    results = ["Draw", "Checkmate", "Abandoned", "Resigned", "Time Forfeit"]
    res_in_range = []


    res_r1 = cumu_elo_res1[timeControl][openingFilter]
    res_r2 = cumu_elo_res2[timeControl][openingFilter]

    # print(res_r1)
    # print(res_r2)

    res_in_range = {res: res_r2.get(res, 0) - res_r1.get(res, 0) for res in results}
    
    return list(res_in_range.values())