#Build player_master.csv from Bowman checklists
import pandas as pd

def create_player_master():
    columns = [
        "player_id",
        "player_name",
        "bowman_first_year",
        "bowman_set",
        "position",
        "bats",
        "throws",
        "birth_date",
        "country",
        "draft_round",
        "draft_pick",
        "international_fa",
        "rookie_year",
        "career_war",
        "all_star_count",
        "hall_of_fame",
        "success_tier"
    ]

    df = pd.DataFrame(columns=columns)

    df.to_csv(
        "data/processed/player_master.csv",
        index=False
    )

if __name__ == "__main__":
    create_player_master()
