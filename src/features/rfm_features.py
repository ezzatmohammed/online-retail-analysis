import pandas as pd

from src.features.build_features import add_revenue
from src.utils.config import CUSTOMER_ID_COLUMN, DATE_COLUMN, INVOICE_COLUMN, REVENUE_COLUMN,QUANTITY_COLUMN


def build_rfm_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if REVENUE_COLUMN not in df.columns:
        df = add_revenue(df)

    df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN])
    df[CUSTOMER_ID_COLUMN] = df[CUSTOMER_ID_COLUMN].astype("Int64")
    df = df.dropna(subset=[CUSTOMER_ID_COLUMN])
    df = df[df[QUANTITY_COLUMN] > 0]
    
    reference_date = df[DATE_COLUMN].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby(CUSTOMER_ID_COLUMN)
        .agg(
            Recency=(
                DATE_COLUMN,
                lambda x: (reference_date - x.max()).days
            ),
            Frequency=(
                INVOICE_COLUMN,
                "nunique"
            ),
            Monetary=(
                REVENUE_COLUMN,
                "sum"
            ),
        )
    )

    return rfm.reset_index()
