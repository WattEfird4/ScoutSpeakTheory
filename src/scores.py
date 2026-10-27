def hall_score_grade(score):

    if score >= 30:
        return "Generational"

    elif score >= 20:
        return "Elite Prospect"

    elif score >= 10:
        return "Strong Prospect"

    elif score >= 0:
        return "Average Prospect"

    return "High Risk Prospect"



#MVP Scores

NEGATIVE_TERMS = {
    # General concerns
    "raw": -3,
    "limited": -4,
    "concerns": -4,
    "injury": -5,

    # Projection risk
    "project": -3,
    "developing": -2,
    "unrefined": -4,
    "inconsistent": -4,

    # Hitting concerns
    "long swing": -4,
    "poor plate discipline": -5,
    "swing and miss": -5,
    "aggressive hitter": -2,

    # Pitching concerns
    "control issues": -5,
    "mechanical issues": -5,
    "reliever profile": -4,

    # Physical/ceiling concerns
    "limited ceiling": -6,
    "undersized": -2,
    "durability concerns": -5,
    "health concerns": -5
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
