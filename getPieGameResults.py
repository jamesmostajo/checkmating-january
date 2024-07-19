import json

jsonfilename = "Cleaning/EloTimeResultsOpenings.json"

def getPieGameresults(ratingFilter1, ratingFilter2, timeControl, openingFilter):

    with open(jsonfilename, 'r') as jsonfile:
        cumu_elo_res = json.load(jsonfile)

    ratingFilter1 -= 1

    r1, r2 = str(ratingFilter1), str(ratingFilter2)

    results = ["Draw", "Checkmate", "Abandoned", "Resigned", "Time Forfeit"]
    res_in_range = []
    
    def get_result_count(elo, tControl, opening):
        if elo in cumu_elo_res:
            if tControl in cumu_elo_res[elo]:
                if opening in cumu_elo_res[elo][tControl]:
                    return cumu_elo_res[elo][tControl][opening]
                elif opening == "All":
                    return cumu_elo_res[elo][tControl]["All"]
            elif tControl == "All":
                if opening in cumu_elo_res[elo]["All"]:
                    return cumu_elo_res[elo]["All"][opening]
                elif opening == "All":
                    return cumu_elo_res[elo]["All"]["All"]
        return {res: 0 for res in results}

    res_r2 = get_result_count(r2, timeControl, openingFilter)
    res_r1 = get_result_count(r1, timeControl, openingFilter)

    res_in_range = {res: res_r2.get(res, 0) - res_r1.get(res, 0) for res in results}
    
    return list(res_in_range.values())