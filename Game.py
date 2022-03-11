import re
import pandas as pd

class Game:
    def process_pgn(self, raw_pgn):
        raw_pgn = raw_pgn.split("\n")[-2]
        raw_pgn = re.sub("\{\[%clk \d+:\d+:\d+(.\d+)?\]\}", '', raw_pgn)
        raw_pgn = re.sub ("\d+\.{3}", " ", raw_pgn)
        raw_pgn = re.sub ("\d+\.", " ",raw_pgn)
        pgn = raw_pgn.split()
        return pgn 


    def __init__(self, raw_data):
        self.timestamp = raw_data["end_time"]
        self.white_player = raw_data["white"]["username"]
        self.white_rating = raw_data["white"]["rating"]
        self.black_player = raw_data["black"]["username"]
        self.black_rating = raw_data["black"]["rating"]
        self.white_result = raw_data["white"]["result"]
        self.black_result = raw_data["black"]["result"]
        self.timeclass = raw_data["time_class"]
        self.uuid = raw_data["uuid"]
        self.pgn  = self.process_pgn(raw_data["pgn"])


    def pretty_print(self):
        print("Game",self.uuid, "\n", self.white_player, "(", self.white_rating,") vs.", self.black_player, "(", self.black_rating, ")\n")
        print(self.pgn)
    
    def export_as_dataframe(self):
        return pd.DataFrame([[self.uuid, self.timestamp, self.white_player, self.black_player, self.timeclass, self.white_rating, self.black_rating, self.white_result, self.black_result, self.pgn]],
                   columns=['uuid', 'timestamp','white_player', 'black_player', 'timeclass', 'white_rating', 'black_rating', 'white_result', 'black_result', 'pgn'])



