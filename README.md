# Online Retail Analytics

This project analyzes the Online Retail II transaction dataset and is structured for multiple analytics and machine learning use cases: cleaning, EDA, feature engineering, RFM segmentation, customer clustering, recommendation systems, churn prediction, sales forecasting, and dashboard reporting.

## Structure

```text
online-retail-analytics/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   ├── segmentation/
│   ├── recommendation/
│   ├── forecasting/
│   ├── churn/
│   ├── visualization/
│   └── utils/
├── models/
├── dashboards/
├── reports/
├── requirements.txt
└── main.py
```

## Pipeline

Run the reusable data preparation pipeline:

```bash
python main.py
```

The script reads `data/raw/online_retail_II.csv`, cleans it, builds transaction features, and writes `data/processed/online_retail_cleaned.csv`.

## ML Use Cases

1. RFM segmentation: score customers by recency, frequency, and monetary value.
2. Customer clustering: group customers using behavioral and value features.
3. Recommendation system: recommend products using collaborative and content-based methods.
4. Churn prediction: identify customers at risk of not purchasing again.
5. Sales forecasting: forecast daily or monthly revenue.
6. Dashboard analysis: prepare KPI outputs for Power BI or Streamlit.

## Notebook Roadmap

- `01_data_cleaning.ipynb`
- `02_eda.ipynb` / existing `02_EDA.ipynb`
- `03_feature_engineering.ipynb`
- `04_rfm_segmentation.ipynb`
- `05_customer_clustering.ipynb`
- `06_recommendation_system.ipynb`
- `07_churn_prediction.ipynb`
- `08_sales_forecasting.ipynb`
- `09_dashboard_analysis.ipynb`

Existing notebooks are preserved and can be consolidated into this sequence as the project matures.

## Next Development Steps

1. Finalize business definitions for revenue, GMV, returns, churn, and active customers.
2. Move validated notebook logic into reusable `src/` modules.
3. Train baseline models for clustering, recommendation, churn, and forecasting.
4. Save trained artifacts under `models/`.
5. Build dashboard-ready tables and charts under `dashboards/` and `reports/`.

See `PROJECT_ROADMAP.md` for the phase-by-phase build plan we will follow.
