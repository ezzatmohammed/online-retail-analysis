import pandas as pd
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_customer_clustering_model(n_clusters: int = 5, random_state: int = 42) -> Pipeline:
    """
    Build a customer clustering pipeline with standard scaling and KMeans.
    """
    return Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            ("model", KMeans(n_clusters=n_clusters, random_state=random_state)),
        ]
    )


def fit_customer_clusters(
    features: pd.DataFrame,
    feature_columns: list[str],
    n_clusters: int = 5,
) -> tuple[pd.DataFrame, Pipeline]:
    
    """
    Fit customer clustering pipeline and return
    clustered data and trained model.
    """
    
    model = build_customer_clustering_model(n_clusters=n_clusters)
    labels = model.fit_predict(features[feature_columns])

    clustered = features.copy()
    clustered["Cluster"] = labels.astype(int)
    return clustered, model

