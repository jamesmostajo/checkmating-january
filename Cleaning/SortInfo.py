import csv
import json

csv_file_path = 'Cleaning/info_data.csv'
json_file_path = 'Cleaning/info_data.json'

keys = ["whiteElo", "blackElo", "timeControl", "move", "termination", "result", "opening"]

data = {}

with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        game_id, whiteElo, blackElo, timeControl, lastMove, termination, result, opening = row
        game_id = int(game_id)
        game_data = {
            "whiteElo": int(whiteElo),
            "blackElo": int(blackElo),
            "timeControl": timeControl,
            "move": lastMove,
            "termination": termination,
            "result": result,
            "opening": opening
        }
        data[game_id] = game_data

with open(json_file_path, mode='w') as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data successfully written to {json_file_path}")