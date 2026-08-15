import pandas as pd
import pytest

from data_inspector.analyzer import analyze_dataset, detect_outliers, load_dataset
from data_inspector.report import DatasetReport


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


def test_analyze_dataset_categorical_summary():
    df = pd.DataFrame(
        {
            "city": ["Dortmund", "Essen", "Dortmund", None],
            "score": [10, 20, 30, 40],
        }
    )

    result = analyze_dataset(df)

    city_summary = result["categorical_summary"]["city"]

    assert city_summary["unique_values"] == 2
    assert city_summary["most_frequent"] == "Dortmund"
    assert city_summary["frequency"] == 2


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


def test_load_dataset_rejects_non_csv(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("some text")

    with pytest.raises(ValueError):
        load_dataset(str(file_path))


def test_report_export(tmp_path):
    analysis = {
        "rows": 2,
        "columns": 2,
        "duplicate_rows": 0,
        "missing_values": {"city": 0, "score": 0},
        "missing_percentages": {"city": 0.0, "score": 0.0},
        "data_types": {"city": "str", "score": "int64"},
        "numeric_summary": {
            "score": {
                "mean": 15.0,
                "min": 10.0,
                "max": 20.0,
            }
        },
        "categorical_summary": {
            "city": {
                "unique_values": 2,
                "most_frequent": "Dortmund",
                "frequency": 1,
            }
        },
        "correlations": {
            "score": {
                "score": 1.0,
            }
        },
        "numeric_columns": ["score"],
        "categorical_columns": ["city"],
    }

    outliers = {"score": 0}

    report = DatasetReport(analysis, outliers)
    file_path = report.save(str(tmp_path))

    assert file_path.exists()

    content = file_path.read_text(encoding="utf-8")

    assert "DATA INSPECTOR REPORT" in content
    assert "Dortmund" in content
    assert "Potential Outliers" in content
    assert "Data Types" in content
    assert "Numeric Summary" in content
    assert "Correlations" in content