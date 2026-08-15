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