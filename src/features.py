import pandas as pd


# --- Single Feature ---
def add_total_price(df: pd.DataFrame) -> pd.DataFrame:
    df["TotalPrice"] = df["Quantity"] * df["Price"]
    return df


# --- Grouped Date Features ---
def add_date_features(df: pd.DataFrame) -> pd.DataFrame:
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month
    df["Day"] = df["InvoiceDate"].dt.day

    return df


# --- RFM Features ---
def add_rfm_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Customer ID"] = df["Customer ID"].astype("Int64")

    # remove missing customers (important for RFM)
    df = df.dropna(subset=["Customer ID"])

    latest_date = df["InvoiceDate"].max()

    rfm = df.groupby("Customer ID").agg({
        "InvoiceDate": lambda x: (latest_date - x.max()).days,
        "Invoice": "nunique",
        "Revenue": "sum"
    })

    rfm.columns = ["Recency", "Frequency", "Monetary"]

    return rfm.reset_index()



# --- Pipeline ---
def add_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = add_total_price(df)
    df = add_date_features(df)

    return df
