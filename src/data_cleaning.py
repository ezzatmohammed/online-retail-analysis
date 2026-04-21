import pandas as pd
from .config import PRICE_UPPER_LIMIT, PRICE_LOWER_LIMIT


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply all data cleaning steps extracted from the EDA notebook.
    """

    df = df.copy()

    # --- Missing values ---
    # Check missing values
    print("Missing values before cleaning:\n", df.isnull().sum())

    # Drop rows with missing Description
    df = df[df["Description"].notnull()]

    # Keep Customer ID even if missing (business decision)

    # --- Duplicates ---
    df.drop_duplicates(inplace=True)

    # --- Invalid values ---
    # Apply advanced filtering logic from notebook
    df = df[~(
        (df['Price'] <= 0) |  # Price <= 0 (likely returns or data errors)
        (df['Price'] > 10000) |  # Extreme outliers or high-ticket items
        (
            (df.get('IsCustomerMissing', False) == True) &
            (df.get('IsReturn', False) == True) &
            (df.get('IsDescriptionMissing', False) == True) &
            (df['Quantity'] < 0)
        )
    )]

    # --- Outliers (Price using IQR) ---
    Q1 = df['Price'].quantile(0.25)
    Q3 = df['Price'].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df = df[(df['Price'] >= lower_bound) & (df['Price'] <= upper_bound)]

    print("Missing values after cleaning:\n", df.isnull().sum())

    return df


if __name__ == "__main__":
    # Example usage
    df = pd.read_csv("data.csv")
    cleaned_df = clean_data(df)
    cleaned_df.to_csv("cleaned_data.csv", index=False)
