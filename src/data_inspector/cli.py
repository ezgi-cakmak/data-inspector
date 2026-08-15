import sys

from .analyzer import analyze_dataset, detect_outliers, load_dataset
from .report import DatasetReport
from .visualizer import plot_correlation_heatmap, plot_numeric_distribution


def main():
    """Run the command-line dataset inspection workflow."""
    if len(sys.argv) < 2:
        print("Please provide a CSV file.")
        return

    file_path = sys.argv[1]
    dataset = load_dataset(file_path)
    analysis = analyze_dataset(dataset)
    outliers = detect_outliers(dataset)

    report = DatasetReport(analysis, outliers)

    numeric_columns = [
        column
        for column in analysis["numeric_columns"]
        if "id" not in column.lower()
        and dataset[column].nunique() > 10
    ]

    if numeric_columns:
        column = numeric_columns[0]
        plot_path = plot_numeric_distribution(dataset, column)
        print(f"Distribution plot saved to: {plot_path}")

    heatmap_path = plot_correlation_heatmap(dataset)
    print(f"Correlation heatmap saved to: {heatmap_path}")

    print()

    for line in report.summary_lines():
        print(line)

    print()

    for line in report.missing_value_lines():
        print(line)

    print("\n--- Data Types ---")
    for column, dtype in analysis["data_types"].items():
        print(f"- {column}: {dtype}")

    print("\n--- Numeric Summary ---")
    for column, stats in analysis["numeric_summary"].items():
        print(f"- {column}:")
        print(f"  mean: {stats.get('mean')}")
        print(f"  min: {stats.get('min')}")
        print(f"  max: {stats.get('max')}")

    print()

    for line in report.outlier_lines():
        print(line)

    print("\n--- Correlations ---")
    for column, values in analysis["correlations"].items():
        print(f"- {column}:")
        for other_column, correlation in values.items():
            print(f"  {other_column}: {correlation}")

    print("\n--- Numeric Columns ---")
    for column in analysis["numeric_columns"]:
        print(f"- {column}")

    print("\n--- Categorical Columns ---")
    for column in analysis["categorical_columns"]:
        print(f"- {column}")

    print("\n--- Column Names ---")
    for column in dataset.columns:
        print(f"- {column}")