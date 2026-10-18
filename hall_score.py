#Generate Hall Score

import pandas as pd

def hall_score(probability):

    return round(probability * 100, 1)

if __name__ == "__main__":

    example_probability = 0.83

    print(
        f"Hall Score: {hall_score(example_probability)}"
    )
