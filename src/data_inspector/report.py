class DatasetReport:
    def __init__(self, analysis: dict, outliers: dict):
        self.analysis = analysis
        self.outliers = outliers

    def summary_lines(self) -> list[str]:
        lines = [
            "=== DATA INSPECTOR REPORT ===",
            f"Rows: {self.analysis['rows']}",
            f"Columns: {self.analysis['columns']}",
            f"Duplicate rows: {self.analysis['duplicate_rows']}",
        ]
        return lines

    def missing_value_lines(self) -> list[str]:
        lines = ["--- Missing Values ---"]

        for column, count in self.analysis["missing_values"].items():
            percentage = self.analysis["missing_percentages"][column]
            lines.append(f"- {column}: {count} ({percentage}%)")

        return lines

    def outlier_lines(self) -> list[str]:
        lines = ["--- Potential Outliers ---"]

        for column, count in self.outliers.items():
            lines.append(f"- {column}: {count}")

        return lines