from urllib import response
import requests
from Game import Game
import pandas as pd
from tqdm import tqdm

def fetch_games(username):
    r = requests.get(f"https://api.chess.com/pub/player/{username.lower()}/games/archives")

    archives = r.json()["archives"]
    list_df = []

    for month in tqdm(archives):
        archive_of_month = requests.get(month).json()
        for element in tqdm(archive_of_month["games"]):
            game = Game(element)
            list_df.append(game.export_as_dataframe())

    df = pd.concat(list_df)
    df.to_csv(f"games/{username.lower()}.csv", index=False)