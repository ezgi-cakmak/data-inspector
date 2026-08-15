# Data Inspector

Data Inspector is a Python command-line tool for performing an initial inspection of CSV datasets. The project was developed as part of the Introduction to Python course at TU Dortmund University.

The goal of the project is to provide a quick overview of an unfamiliar dataset before performing more detailed data analysis.

## Features

Data Inspector currently provides:

- dataset dimensions
- column names and data types
- missing-value counts and percentages
- duplicate-row detection
- separation of numerical and categorical columns
- descriptive statistics for numerical variables
- IQR-based potential outlier detection
- correlation analysis
- automatic distribution plots for suitable numerical variables
- a correlation heatmap

## Installation

Clone the repository and install the project from the project directory:

```bash
pip install -e .
```

To install the dependencies required for running the tests:

```bash
pip install -e ".[test]"
```

## Usage

Run Data Inspector from the project directory and provide the path to a CSV file:

```bash
python -m data_inspector path/to/dataset.csv
```

For example:

```bash
python -m data_inspector data/titanic.csv
```

The program prints an analysis report to the terminal and saves generated visualizations in the `plots/` directory.

## Testing

The project uses pytest for automated testing.

Run the test suite with:

```bash
pytest
```

## Project Structure

```text
data-inspector/
├── src/
│   └── data_inspector/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py
│       ├── cli.py
│       └── visualizer.py
├── tests/
│   └── test_analyzer.py
├── data/
├── notebooks/
├── pyproject.toml
└── README.md
```

## Technologies

- Python
- pandas
- Matplotlib
- pytest

## Current Limitations

The current version supports CSV files only. Outlier detection uses the IQR method and should be interpreted as an indication of potentially unusual observations rather than an automatic classification of errors.