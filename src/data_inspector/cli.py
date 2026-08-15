import sys

from .analyzer import load_dataset, analyze_dataset, detect_outliers
from .visualizer import plot_numeric_distribution, plot_correlation_heatmap


def main():
   if len(sys.argv) < 2:
       print("Please provide a CSV file.")
       return

   file_path = sys.argv[1]
   dataset = load_dataset(file_path)
   analysis = analyze_dataset(dataset)
   outliers = detect_outliers(dataset)
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

   print(f"Rows: {analysis['rows']}")
   print(f"Columns: {analysis['columns']}")
   print(f"Duplicate rows: {analysis['duplicate_rows']}")

   print("Missing values:")
   for column, count in analysis["missing_values"].items():
       percentage = analysis["missing_percentages"][column]
       print(f"- {column}: {count} ({percentage}%)")

   print("Data types:")
   for column, dtype in analysis["data_types"].items():
       print(f"- {column}: {dtype}")

   print("Numeric summary:")
   for column, stats in analysis["numeric_summary"].items():
       print(f"- {column}:")
       print(f"  mean: {stats.get('mean')}")
       print(f"  min: {stats.get('min')}")
       print(f"  max: {stats.get('max')}")

   print("Potential outliers:")
   for column, count in outliers.items():
       print(f"- {column}: {count}")

       print("Correlations:")
       for column, values in analysis["correlations"].items():
           print(f"- {column}:")
           for other_column, correlation in values.items():
               print(f"  {other_column}: {correlation}")

   print("Numeric columns:")
   for column in analysis["numeric_columns"]:
       print(f"- {column}")

   print("Categorical columns:")
   for column in analysis["categorical_columns"]:
       print(f"- {column}")

   print("Column names:")
   for column in dataset.columns:
       print(f"- {column}")