#This script will start from a username as a seed and will collect all the games 
#this username played on chess.com as well as all the games its adversaries ever played.

import argparse
from crawler import fetch_games
import pandas as pd


    

def main():
    parser = argparse.ArgumentParser(description='Fetches all the games ever played by a given username on Chess.com\nExport a csv at the end.')
    parser.add_argument('username', metavar='p', type=str,
                        help='The username seed from which you want to start collecting games.')
    parser.add_argument('limit', metavar='l', type=int,
                        help='The maximum number of players you want to collect the games of')
    args = parser.parse_args()

    queue = [args.username]
    collected_players = []

    while len(collected_players) < args.limit:
        username  = queue.pop()
        print(f"Now fetching games of {username}")
        fetch_games(username)
        collected_players.append(username)
        print(f"Fetched all games of {username}, now adding all {username}'s adversaries to the queue.")
        list_other_players = extract_usernames_set(username.lower())
        for player in list_other_players:
            if player not in queue and player not in collected_players:
                queue.append(player)


def extract_usernames_set(filename):
    df = pd.read_csv(f"games/{filename}.csv")
    white = list(df['white_player'])
    black = list(df['black_player'])
    black.extend(white)
    set_players  = set(black)
    return list(set_players)

if __name__ == "__main__":
    main()