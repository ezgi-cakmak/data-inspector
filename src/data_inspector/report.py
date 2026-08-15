from pathlib import Path


class DatasetReport:
    """Format dataset analysis results for terminal output and file export."""

    def __init__(self, analysis: dict, outliers: dict):
        self.analysis = analysis
        self.outliers = outliers

    def summary_lines(self) -> list[str]:
        """Return the general dataset summary."""
        lines = [
            "=== DATA INSPECTOR REPORT ===",
            f"Rows: {self.analysis['rows']}",
            f"Columns: {self.analysis['columns']}",
            f"Duplicate rows: {self.analysis['duplicate_rows']}",
        ]
        return lines

    def missing_value_lines(self) -> list[str]:
        """Return formatted missing-value information."""
        lines = ["--- Missing Values ---"]

        for column, count in self.analysis["missing_values"].items():
            percentage = self.analysis["missing_percentages"][column]
            lines.append(f"- {column}: {count} ({percentage}%)")

        return lines

    def outlier_lines(self) -> list[str]:
        """Return formatted potential-outlier information."""
        lines = ["--- Potential Outliers ---"]

        for column, count in self.outliers.items():
            lines.append(f"- {column}: {count}")

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

    def all_lines(self) -> list[str]:
        """Return the complete report as a list of text lines."""
        lines = []

        lines.extend(self.summary_lines())
        lines.append("")
        lines.extend(self.missing_value_lines())
        lines.append("")
        lines.extend(self.categorical_summary_lines())
        lines.append("")
        lines.extend(self.outlier_lines())

        return lines

    def save(self, output_dir: str = "reports") -> Path:
        """Save the formatted report to a text file."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        file_path = output_path / "data_inspector_report.txt"
        file_path.write_text("\n".join(self.all_lines()) + "\n", encoding="utf-8")

        return file_path