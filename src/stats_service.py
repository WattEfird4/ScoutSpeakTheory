from pathlib import Path
from datetime import datetime, timedelta
from pybaseball import batting_stats
import pandas as pd

CACHE_DIR = Path("data/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

CACHE_FILE = CACHE_DIR / "batting_stats.parquet"

CACHE_DAYS = 7


def cache_is_fresh():
    if not CACHE_FILE.exists():
        return False

    modified = datetime.fromtimestamp(
        CACHE_FILE.stat().st_mtime
    )

    age = datetime.now() - modified

    return age < timedelta(days=CACHE_DAYS)


def get_batting_stats():

    if cache_is_fresh():
        print("Using cached stats")
        return pd.read_parquet(CACHE_FILE)

    print("Downloading fresh stats")

    stats = batting_stats(
        2000,
        datetime.now().year,
        qual=0
    )

    stats.to_parquet(CACHE_FILE)

    return stats
