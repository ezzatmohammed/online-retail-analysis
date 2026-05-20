import pandas as pd


def score_rfm(
    rfm: pd.DataFrame,
    recency_col: str = "Recency",
    frequency_col: str = "Frequency",
    monetary_col: str = "Monetary",
) -> pd.DataFrame:

    scored = rfm.copy()

    # Recency → lower is better
    scored["R_Score"] = pd.qcut(
        scored[recency_col],
        q=5,
        labels=[5,4,3,2,1],
        duplicates="drop"
    )

    scored["R_Score"] = (
        scored["R_Score"].max()
        - scored["R_Score"]
    ) + 1


    # Frequency → higher is better
    scored["F_Score"] = (
        pd.qcut(
            scored[frequency_col],
            q=4,
            labels=False,
            duplicates="drop"
        ) + 1
    )


    # Monetary → higher is better
    scored["M_Score"] = (
        pd.qcut(
            scored[monetary_col],
            q=5,
            labels=False,
            duplicates="drop"
        ) + 1
    )


    # Combine scores
    scored["RFM_Score"] = (
        scored["R_Score"].astype(str)
        + scored["F_Score"].astype(str)
        + scored["M_Score"].astype(str)
    )

    return scored


def assign_rfm_segment(row: pd.Series) -> str:
    r = int(row["R_Score"])
    f = int(row["F_Score"])
    m = int(row["M_Score"])

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"
    if r >= 3 and f >= 3:
        return "Loyal Customers"
    if r >= 4 and f <= 2:
        return "New Customers"
    if r <= 2 and f >= 3:
        return "At Risk"
    if r <= 2 and f <= 2:
        return "Lost"
    return "Needs Attention"


def add_rfm_segments(scored_rfm: pd.DataFrame) -> pd.DataFrame:
    segmented = scored_rfm.copy()

    segmented["Segment"] = segmented.apply(
        assign_rfm_segment,
        axis=1
    )

    return segmented