import pandas as pd

class AnimeDataLoader:
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8", on_bad_lines='skip').dropna()
        required_cols = { 'Name', 'Genres', 'sypnopsis' }

        missing = required_cols - set(df.columns)
        if missing:
            raise ValueError(f"Missing column in CSV File.")

        df['combined_info'] = (
            "Title: " + df["Name"] + " Overview: " +df["sypnopsis"] + "Genres : " + df["Genres"]
        )

        # Exporting a new csv with combined_info column
        # Select only the 'combined_info' column from the DataFrame and export it to a new CSV file.
        # The output CSV will be saved at the path specified by self.processed_csv.
        # The index is not included in the output file, and UTF-8 encoding is used.
        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding="utf-8")

        return self.processed_csv