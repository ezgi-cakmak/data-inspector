import pandas as pd

from data_inspector.analyzer import analyze_dataset, detect_outliers, load_dataset


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


def test_detect_outliers():
    df = pd.DataFrame(
        {
            "value": [10, 11, 12, 13, 14, 15, 100],
        }
    )

    result = detect_outliers(df)

    assert result["value"] == 1


def test_load_dataset(tmp_path):
    file_path = tmp_path / "sample.csv"
    file_path.write_text("age,score\n20,80\n25,90\n")

    df = load_dataset(str(file_path))

    assert len(df) == 2
    assert list(df.columns) == ["age", "score"]