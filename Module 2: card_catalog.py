import pandas as pd


class CardCatalog:

    def load_catalog(self, file_path):

        return pd.read_csv(file_path)

    def get_unprocessed_cards(self, df):

        return df[df["ocr_complete"] == False]
