import pandas as pd
from pathlib import Path
from typing import List, Optional, Dict, Any

import matplotlib.pyplot as plt


class ThesisDataAnalyzer:
    def __init__(self) -> None:
        self.data: Optional[pd.DataFrame] = None
        self.summary: Optional[pd.DataFrame] = None

    def load_data(self, file_path: str) -> pd.DataFrame:
        path = Path(file_path)
        suffix = path.suffix.lower()
        if suffix == ".csv":
            self.data = pd.read_csv(path)
        elif suffix in {".xls", ".xlsx"}:
            self.data = pd.read_excel(path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel files.")
        return self.data

    def get_numeric_columns(self) -> List[str]:
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        numeric_cols = self.data.select_dtypes(include=["number"]).columns.tolist()
        return numeric_cols

    def calculate_statistics(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        numeric_cols = columns if columns is not None else self.get_numeric_columns()
        if not numeric_cols:
            raise ValueError("No numeric columns found in the dataset.")

        stats = self.data[numeric_cols].describe().transpose()
        stats = stats.rename(columns={
            "count": "count",
            "mean": "mean",
            "std": "std",
            "min": "min",
            "25%": "25%",
            "50%": "median",
            "75%": "75%",
            "max": "max",
        })
        self.summary = stats
        return stats

    def generate_histograms(
        self,
        output_dir: str,
        columns: Optional[List[str]] = None,
        bins: int = 20,
    ) -> List[str]:
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        output_dir_path = Path(output_dir)
        output_dir_path.mkdir(parents=True, exist_ok=True)

        numeric_cols = columns if columns is not None else self.get_numeric_columns()
        chart_paths: List[str] = []
        for column in numeric_cols:
            series = self.data[column].dropna()
            if series.empty:
                continue
            plt.figure(figsize=(8, 5))
            plt.hist(series, bins=bins, color="#2a8fbd", edgecolor="#333333", alpha=0.9)
            plt.title(f"Histogram: {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.grid(True, linestyle="--", alpha=0.4)
            chart_path = output_dir_path / f"histogram_{column}.png"
            plt.tight_layout()
            plt.savefig(chart_path)
            plt.close()
            chart_paths.append(str(chart_path))
        return chart_paths

    def generate_scatter_plots(
        self,
        output_dir: str,
        x_column: str,
        y_column: str,
        bins: int = 20,
    ) -> str:
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        output_dir_path = Path(output_dir)
        output_dir_path.mkdir(parents=True, exist_ok=True)

        if x_column not in self.data.columns or y_column not in self.data.columns:
            raise ValueError("Selected columns are not available in the data.")
        plt.figure(figsize=(8, 5))
        plt.scatter(self.data[x_column], self.data[y_column], alpha=0.6, color="#2a8fbd")
        plt.title(f"Scatter plot: {x_column} vs {y_column}")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True, linestyle="--", alpha=0.4)
        chart_path = output_dir_path / f"scatter_{x_column}_vs_{y_column}.png"
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
        return str(chart_path)

    def export_summary_to_excel(self, output_file: str) -> str:
        if self.summary is None:
            raise ValueError("Summary statistics not calculated. Call calculate_statistics() first.")
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            self.summary.to_excel(writer, sheet_name="summary_stats")
            if self.data is not None:
                self.data.to_excel(writer, sheet_name="raw_data", index=False)
        return str(output_path)

    def get_summary_dict(self) -> Dict[str, Any]:
        if self.summary is None:
            raise ValueError("Summary statistics not calculated. Call calculate_statistics() first.")
        return self.summary.reset_index().rename(columns={"index": "column"}).to_dict(orient="records")
