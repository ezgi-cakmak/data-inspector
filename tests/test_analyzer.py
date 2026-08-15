import pandas as pd

from data_inspector.analyzer import analyze_dataset


def test_analyze_dataset_basic_information():
   df = pd.DataFrame(
       {
           "age": [20, 25, 30],
           "score": [80, 90, 100],
       }
   )

   result = analyze_dataset(df)

   assert result["rows"] == 3
   assert result["columns"] == 2
   assert result["duplicate_rows"] == 0


def test_analyze_dataset_missing_values():
   df = pd.DataFrame(
       {
           "age": [20, None, 30],
           "score": [80, 90, None],
       }
   )

   result = analyze_dataset(df)

   assert result["missing_values"]["age"] == 1
   assert result["missing_values"]["score"] == 1
   assert result["missing_percentages"]["age"] == 33.33
   assert result["missing_percentages"]["score"] == 33.33