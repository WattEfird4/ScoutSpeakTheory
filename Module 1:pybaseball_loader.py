from pybaseball import playerid_lookup
import pandas as pd


class PyBaseballLoader:

    def get_player_id(self, first_name, last_name):

        try:
            results = playerid_lookup(last_name, first_name)

            if len(results) == 0:
                return None

            return results.iloc[0]["key_mlbam"]

        except:
            return None
