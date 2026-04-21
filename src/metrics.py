def calculate_gmv(df):
    return (df["Quantity"] * df["Price"]).sum()


def return_rate(df):
    returns = df[df["Quantity"] < 0]
    return len(returns) / len(df)


def average_order_value(df):
    return df.groupby("Invoice")["Quantity"].sum().mean()
