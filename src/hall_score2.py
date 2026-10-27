#Generate Hall Score

import pandas as pd

# src/hall_score.py

POSITIVE_TERMS = {

    # Elite ceiling indicators
    "elite": 8,
    "generational": 10,
    "exceptional": 8,
    "special": 7,
    "impact": 7,
    "superstar": 10,

    # Hitting
    "advanced": 5,
    "approach": 4,
    "bat speed": 6,
    "plate discipline": 6,
    "hit tool": 5,
    "strike zone awareness": 5,
    "contact": 3,
    "power": 4,
    "plus power": 7,
    "plus-plus power": 10,

    # Athleticism
    "athletic": 4,
    "athleticism": 5,
    "explosive": 5,
    "quick": 3,
    "speed": 3,
    "five-tool": 10,

    # Baseball IQ
    "instincts": 6,
    "baseball instincts": 8,
    "leadership": 5,
    "makeup": 6,
    "competitor": 4,
    "work ethic": 5,
    "coachable": 4,

    # Pitchers
    "live arm": 7,
    "command": 5,
    "plus fastball": 7,
    "plus breaking ball": 7,
    "durable": 5,
    "repeatable delivery": 6,
    "projectable frame": 5,

    # General projections
    "all-star": 8,
    "frontline": 9,
    "ace": 10,
    "middle-of-the-order": 8,
    "run producer": 5,
}


NEGATIVE_TERMS = {

    # Development risk
    "raw": -4,
    "project": -5,
    "developing": -2,
    "inconsistent": -5,
    "unrefined": -5,

    # Physical concerns
    "injury": -8,
    "durability concerns": -7,
    "health concerns": -7,

    # Performance concerns
    "limited": -5,
    "limited ceiling": -8,
    "swing and miss": -6,
    "poor plate discipline": -6,
    "struggles": -4,

    # Projection concerns
    "questionable": -6,
    "concerns": -4,
    "risk": -5,
    "mechanical issues": -6,
    "control problems": -6,
    "reliever profile": -5,

    # Scouting red flags
    "aggressive at the plate": -2,
    "long swing": -5,
    "lack of consistency": -5,
    "defensive limitations": -5
}

def calculate_hall_score(text):

    text = text.lower()

    score = 0

    for phrase, weight in POSITIVE_TERMS.items():
        if phrase in text:
            score += weight

    for phrase, weight in NEGATIVE_TERMS.items():
        if phrase in text:
            score += weight

    return score
