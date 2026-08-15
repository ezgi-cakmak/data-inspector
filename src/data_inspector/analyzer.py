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
    """Compute basic data quality checks and exploratory statistics."""
    numeric_df = df.select_dtypes(include="number")

    numeric_summary = (
        numeric_df.describe().to_dict()
        if not numeric_df.empty
        else {}
    )

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "missing_percentages": (df.isnull().mean() * 100).round(2).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
        "numeric_summary": numeric_summary,
        "numeric_columns": numeric_df.columns.tolist(),
        "categorical_columns": df.select_dtypes(exclude="number").columns.tolist(),
        "categorical_summary": summarize_categorical_columns(df),
        "correlations": numeric_df.corr().round(2).to_dict(),
    }


def summarize_categorical_columns(df: pd.DataFrame) -> dict:
    """Summarize categorical columns using unique and most frequent values."""
    summary = {}

    categorical_columns = df.select_dtypes(exclude="number").columns

    for column in categorical_columns:
        non_missing_values = df[column].dropna()
        value_counts = non_missing_values.value_counts()

        if value_counts.empty:
            most_frequent = None
            frequency = 0
        else:
            most_frequent = value_counts.index[0]
            frequency = int(value_counts.iloc[0])

        summary[column] = {
            "unique_values": int(non_missing_values.nunique()),
            "most_frequent": most_frequent,
            "frequency": frequency,
        }

    return summary


def detect_outliers(df: pd.DataFrame) -> dict:
    """Count potential outliers in numeric columns using the IQR rule."""
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