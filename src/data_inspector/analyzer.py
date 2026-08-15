from pathlib import Path

import pandas as pd


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load a CSV file and return it as a pandas DataFrame."""
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix.lower() != ".csv":
        raise ValueError("Only CSV files are currently supported.")

    return pd.read_csv(path)

def analyze_dataset(df: pd.DataFrame) -> dict:
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_percentages": (df.isnull().mean() * 100).round(2).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
        "numeric_summary": df.describe().to_dict(),
        "numeric_columns": df.select_dtypes(include="number").columns.tolist(),
        "categorical_columns": df.select_dtypes(exclude="number").columns.tolist(),
        "correlations": df.select_dtypes(include="number").corr().round(2).to_dict(),
    }

def detect_outliers(df: pd.DataFrame) -> dict:
    outliers = {}

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        count = ((df[column] < lower_bound) | (df[column] > upper_bound)).sum()
        outliers[column] = int(count)

    return outliers