from pathlib import Path


class DatasetReport:
    """Format dataset analysis results for terminal output and file export."""

    def __init__(self, analysis: dict, outliers: dict):
        self.analysis = analysis
        self.outliers = outliers

    def summary_lines(self) -> list[str]:
        """Return the general dataset summary."""
        return [
            "=== DATA INSPECTOR REPORT ===",
            f"Rows: {self.analysis['rows']}",
            f"Columns: {self.analysis['columns']}",
            f"Duplicate rows: {self.analysis['duplicate_rows']}",
        ]

    def missing_value_lines(self) -> list[str]:
        """Return formatted missing-value information."""
        lines = ["--- Missing Values ---"]

        for column, count in self.analysis["missing_values"].items():
            percentage = self.analysis["missing_percentages"][column]
            lines.append(f"- {column}: {count} ({percentage}%)")

        return lines

    def data_type_lines(self) -> list[str]:
        """Return formatted data-type information."""
        lines = ["--- Data Types ---"]

        for column, dtype in self.analysis["data_types"].items():
            lines.append(f"- {column}: {dtype}")

        return lines

    def numeric_summary_lines(self) -> list[str]:
        """Return formatted descriptive statistics for numeric columns."""
        lines = ["--- Numeric Summary ---"]

        for column, stats in self.analysis["numeric_summary"].items():
            lines.append(f"- {column}:")
            lines.append(f"  mean: {stats.get('mean')}")
            lines.append(f"  min: {stats.get('min')}")
            lines.append(f"  max: {stats.get('max')}")

        return lines

    def categorical_summary_lines(self) -> list[str]:
        """Return formatted summaries for categorical columns."""
        lines = ["--- Categorical Summary ---"]

        for column, stats in self.analysis["categorical_summary"].items():
            lines.append(f"- {column}:")
            lines.append(f"  unique values: {stats['unique_values']}")
            lines.append(f"  most frequent: {stats['most_frequent']}")
            lines.append(f"  frequency: {stats['frequency']}")

        return lines

    def outlier_lines(self) -> list[str]:
        """Return formatted potential-outlier information."""
        lines = ["--- Potential Outliers ---"]

        for column, count in self.outliers.items():
            lines.append(f"- {column}: {count}")

        return lines

    def correlation_lines(self) -> list[str]:
        """Return formatted correlation information."""
        lines = ["--- Correlations ---"]

        for column, values in self.analysis["correlations"].items():
            lines.append(f"- {column}:")
            for other_column, correlation in values.items():
                lines.append(f"  {other_column}: {correlation}")

        return lines

    def column_group_lines(self) -> list[str]:
        """Return formatted numeric and categorical column lists."""
        lines = ["--- Numeric Columns ---"]

        for column in self.analysis["numeric_columns"]:
            lines.append(f"- {column}")

        lines.append("")
        lines.append("--- Categorical Columns ---")

        for column in self.analysis["categorical_columns"]:
            lines.append(f"- {column}")

        return lines

    def all_lines(self) -> list[str]:
        """Return the complete report as a list of text lines."""
        sections = [
            self.summary_lines(),
            self.missing_value_lines(),
            self.data_type_lines(),
            self.numeric_summary_lines(),
            self.categorical_summary_lines(),
            self.outlier_lines(),
            self.correlation_lines(),
            self.column_group_lines(),
        ]

        lines = []

        for index, section in enumerate(sections):
            if index > 0:
                lines.append("")
            lines.extend(section)

        return lines

    def save(self, output_dir: str = "reports") -> Path:
        """Save the complete formatted report to a text file."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / "data_inspector_report.txt"
        file_path.write_text(
            "\n".join(self.all_lines()) + "\n",
            encoding="utf-8",
        )

        return file_path