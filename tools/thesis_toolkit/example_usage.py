from pathlib import Path

from tools.thesis_toolkit.analyzer import ThesisDataAnalyzer
from tools.thesis_toolkit.report_generator import ThesisReportGenerator


def run_example():
    example_path = Path(__file__).resolve().parent / "example_data.xlsx"
    analyzer = ThesisDataAnalyzer()
    data = analyzer.load_data(str(example_path))

    print("Loaded data with shape:", data.shape)
    print("Numeric columns:", analyzer.get_numeric_columns())

    summary = analyzer.calculate_statistics()
    print(summary)

    output_dir = Path(__file__).resolve().parent / "output"
    hist_paths = analyzer.generate_histograms(str(output_dir))
    print("Generated histograms:", hist_paths)

    if len(analyzer.get_numeric_columns()) >= 2:
        scatter_path = analyzer.generate_scatter_plots(
            str(output_dir),
            x_column=analyzer.get_numeric_columns()[0],
            y_column=analyzer.get_numeric_columns()[1],
        )
        print("Generated scatter:", scatter_path)

    excel_path = analyzer.export_summary_to_excel(str(output_dir / "thesis_summary.xlsx"))
    print("Exported summary to:", excel_path)

    report = ThesisReportGenerator(title="BCELP Thesis Toolkit Report")
    report.add_description("Generated summary statistics and charts from the provided dataset.")
    report.add_summary_table(analyzer.get_summary_dict())
    for chart in hist_paths:
        report.add_image(chart, caption=f"Chart: {Path(chart).name}")
    report_path = report.save(str(output_dir / "thesis_report.docx"))
    print("Generated report:", report_path)


if __name__ == "__main__":
    run_example()
