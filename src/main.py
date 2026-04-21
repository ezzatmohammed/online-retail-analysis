import pandas as pd
from src import clean_data, add_features


def main():
    df = pd.read_csv("data/raw/data.csv")

    df = clean_data(df)
    df = add_features(df)

    df.to_csv("data/processed/cleaned_data.csv", index=False)


if __name__ == "__main__":
    main()
