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
