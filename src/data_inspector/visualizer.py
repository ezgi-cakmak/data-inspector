from pathlib import Path

import matplotlib.pyplot as plt

def plot_numeric_distribution(df, column: str, output_dir: str = "plots"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plt.figure()
    df[column].dropna().hist(bins=20)
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()

    file_path = output_path / f"{column}_distribution.png"
    plt.savefig(file_path)
    plt.close()

    return file_path

def plot_correlation_heatmap(df, output_dir: str = "plots"):
    numeric_df = df.select_dtypes(include="number")
    correlation_matrix = numeric_df.corr()

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 6))
    image = plt.imshow(correlation_matrix, aspect="auto")

    plt.colorbar(image)
    plt.xticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
        rotation=45,
        ha="right",
    )
    plt.yticks(
        range(len(correlation_matrix.columns)),
        correlation_matrix.columns,
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()

    file_path = output_path / "correlation_heatmap.png"
    plt.savefig(file_path)
    plt.close()

    return file_path