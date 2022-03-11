from urllib import response
import requests
from Game import Game
import pandas as pd
from tqdm import tqdm

def fetch_games(username):
    r = requests.get(f"https://api.chess.com/pub/player/{username.lower()}/games/archives")

    archives = r.json()["archives"]
    list_df = []
    count_games =0
    for month in tqdm(archives):
        archive_of_month = requests.get(month).json()
        for element in tqdm(archive_of_month["games"]):
            if element["time_class"] == "rapid":
                game = Game(element)
                list_df.append(game.export_as_dataframe())
                count_games +=1
                if count_games >= 100:
                    break

        if count_games >= 100:
            break

    df = pd.concat(list_df)
    df.to_csv(f"games/{username.lower()}.csv", index=False)