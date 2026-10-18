#Find undervalued prospects
def mispricing_score(
    language_score,
    market_score
):

    return language_score - market_score

if __name__ == "__main__":

    language = 87
    market = 65

    score = mispricing_score(
        language,
        market
    )

    print(score)
