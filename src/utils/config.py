from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"

RAW_DATA_PATH = RAW_DATA_DIR / "online_retail_II.csv"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "online_retail_cleaned.csv"

PRICE_LOWER_LIMIT = 0
PRICE_UPPER_LIMIT = 10000

CUSTOMER_ID_COLUMN = "Customer ID"
INVOICE_COLUMN = "Invoice"
PRODUCT_ID_COLUMN = "StockCode"
DATE_COLUMN = "InvoiceDate"
QUANTITY_COLUMN = "Quantity"
PRICE_COLUMN = "Price"
REVENUE_COLUMN = "Revenue"
