import sys

from .analyzer import load_dataset, analyze_dataset


def main():
   if len(sys.argv) < 2:
       print("Please provide a CSV file.")
       return

   file_path = sys.argv[1]
   dataset = load_dataset(file_path)
   analysis = analyze_dataset(dataset)

   print(f"Rows: {analysis['rows']}")
   print(f"Columns: {analysis['columns']}")
   print(f"Duplicate rows: {analysis['duplicate_rows']}")

   print("Missing values:")
   for column, count in analysis["missing_values"].items():
       print(f"- {column}: {count}")

   print("Data types:")
   for column, dtype in analysis["data_types"].items():
       print(f"- {column}: {dtype}")

   print("Numeric summary:")
   for column, stats in analysis["numeric_summary"].items():
       print(f"- {column}:")
       print(f"  mean: {stats.get('mean')}")
       print(f"  min: {stats.get('min')}")
       print(f"  max: {stats.get('max')}")

   print("Numeric columns:")
   for column in analysis["numeric_columns"]:
       print(f"- {column}")

   print("Categorical columns:")
   for column in analysis["categorical_columns"]:
       print(f"- {column}")

   print("Column names:")
   for column in dataset.columns:
       print(f"- {column}")