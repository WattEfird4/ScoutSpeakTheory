import pandas as pd

df = pd.read_csv(
    "data/processed/player_stats.csv"
)

df["WAR"] = df["WAR"].fillna(0)
df["HR"] = df["HR"].fillna(0)
df["RBI"] = df["RBI"].fillna(0)
df["G"] = df["G"].fillna(0)

df["speakscout_score"] = (
      df["WAR"] * 0.6
    + df["HR"] * 0.1
    + df["RBI"] * 0.05
    + df["G"] * 0.02
)

df.sort_values(
    "speakscout_score",
    ascending=False,
    inplace=True
)

df.to_csv(
    "results/player_scores.csv",
    index=False
)

print("Scores generated")
