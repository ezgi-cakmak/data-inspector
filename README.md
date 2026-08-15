# Data Inspector

Data Inspector is a Python command-line tool for performing an initial inspection of CSV datasets. The project was developed as part of the Introduction to Python course at TU Dortmund University.

The goal of the project is to provide a quick overview of an unfamiliar dataset before performing more detailed data analysis.

## Features

Data Inspector provides:

- dataset dimensions
- column names and data types
- missing-value counts and percentages
- duplicate-row detection
- separation of numerical and categorical columns
- descriptive statistics for numerical variables
- summaries of categorical variables, including unique and most frequent values
- IQR-based potential outlier detection
- correlation analysis
- automatic distribution plots for suitable numerical variables
- a correlation heatmap
- formatted command-line reports
- automatic export of the analysis report to a text file

## Example Output

Data Inspector automatically generates visualizations for numerical data.

### Numeric Distribution

The following example shows the distribution of a numerical variable:

![Example numeric distribution](plots/Age_distribution.png)

### Correlation Heatmap

The correlation heatmap provides an overview of linear relationships between numerical variables:

![Example correlation heatmap](plots/correlation_heatmap.png)

## Installation

Clone the repository and install the package from the project directory:

```bash
uv pip install -e .
```

To install the optional dependencies required for testing:

```bash
uv pip install -e ".[test]"
```

## Usage

Run Data Inspector from the project directory and provide the path to a CSV dataset:

```bash
uv run -m data_inspector path/to/dataset.csv
```

For example:

```bash
uv run -m data_inspector my_dataset.csv
```

Data Inspector prints the analysis report directly to the terminal.

Generated visualizations are saved automatically in the `plots/` directory. A text summary of the analysis is also exported to `reports/data_inspector_report.txt`.

## Analysis Report

The analysis report contains:

- number of rows and columns
- duplicate-row count
- missing-value counts and percentages
- detected data types
- descriptive statistics for numerical variables
- summaries of categorical variables
- potential outlier counts
- correlations between numerical variables
- numerical and categorical column lists

## Testing

The project uses `pytest` for automated testing.

Run the complete test suite with:

```bash
uv run pytest
```

The tests cover:

- basic dataset analysis
- missing-value calculations
- categorical column summaries
- IQR-based outlier detection
- CSV file loading
- validation of unsupported file formats
- text report export

## Project Structure

```text
data-inspector/
├── src/
│   └── data_inspector/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       ├── cli.py
│       ├── report.py
│       └── visualizer.py
├── tests/
│   └── test_analyzer.py
├── plots/
│   ├── Age_distribution.png
│   └── correlation_heatmap.png
├── reports/
│   └── data_inspector_report.txt
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Design Decisions

The project was designed as a small reusable Python package rather than a single analysis script. Dataset analysis, visualization, report generation, and command-line execution are separated into different modules so that each component has a clear responsibility and can be reused independently.

The IQR method was selected for potential outlier detection because it is simple, interpretable, and does not assume that the data follows a normal distribution. Detected values are therefore reported as potential outliers rather than automatically treated as errors.

Numerical and categorical columns are handled separately because they require different types of summaries. Numerical variables are used for descriptive statistics, correlations, and visualizations, while categorical variables are summarized using their number of unique values and most frequent observations.

The program also handles datasets without numerical columns. In this case, numerical visualizations and correlation analysis are skipped when they are not applicable, while the remaining dataset inspection continues normally.

CSV was chosen as the supported input format to keep the scope focused on the core goals of the project. Support for additional formats could be added in future versions without changing the overall package structure.

## Package Design

The project is organized into reusable components.

### Analyzer

`analyzer.py` contains functions for:

- loading CSV datasets
- performing basic dataset analysis
- calculating missing-value statistics
- generating summaries for categorical variables
- calculating correlations
- detecting potential outliers using the IQR method

### Visualizer

`visualizer.py` contains reusable functions for generating and saving:

- numerical distribution plots
- correlation heatmaps

### Report

`report.py` contains the `DatasetReport` class, which formats analysis results for command-line output and exports a text report to the `reports/` directory.

### Command-Line Interface

`cli.py` coordinates dataset loading, analysis, visualization, report generation, and report export.

`__main__.py` allows the package to be executed directly with:

```bash
uv run -m data_inspector path/to/dataset.csv
```

The main package components are exposed through `data_inspector.__init__`.

## Technologies

The project uses:

- Python 3.10+
- pandas
- Matplotlib
- pytest
- uv

## Current Limitations

The current version supports CSV files only.

Potential outliers are identified using the IQR rule. These observations should be interpreted as potentially unusual values that may require further investigation rather than automatically being classified as data errors.

Correlation analysis is performed only for numerical columns and represents linear relationships between variables.

## Future Improvements

Possible extensions of the project include:

- support for additional file formats such as Excel and JSON
- configurable visualization options
- additional statistical summaries
- more advanced data-quality checks