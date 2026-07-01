# BCELP Thesis Toolkit

A lightweight utility for processing automotive and electromobility test data from CSV or Excel files.

## Features

- Load CSV or Excel test files
- Detect numeric columns automatically
- Calculate basic summary statistics
- Generate histogram and scatter plot PNG charts
- Export summary and raw data to Excel
- Generate a simple Word report with tables and charts

## Requirements

- pandas
- openpyxl
- matplotlib
- python-docx

## Installation

Install the dependencies in your Python environment:

```bash
pip install pandas openpyxl matplotlib python-docx
```

## Usage

```bash
python tools/thesis_toolkit/example_usage.py
```

## Example

```python
from thesis_toolkit.analyzer import ThesisDataAnalyzer
from thesis_toolkit.report_generator import ThesisReportGenerator

analyzer = ThesisDataAnalyzer()
data = analyzer.load_data("path/to/test_data.xlsx")
print("Numeric columns:", analyzer.get_numeric_columns())
summary = analyzer.calculate_statistics()
print(summary)

output_dir = "tools/thesis_toolkit/output"
charts = analyzer.generate_histograms(output_dir)
print("Charts saved to:", charts)

excel_path = analyzer.export_summary_to_excel("tools/thesis_toolkit/output/thesis_summary.xlsx")
print("Summary saved to:", excel_path)

report = ThesisReportGenerator("Thesis Toolkit Report")
report.add_description("Basic analysis output for thesis data.")
report.add_summary_table(analyzer.get_summary_dict())
for chart in charts:
    report.add_image(chart)
report_path = report.save("tools/thesis_toolkit/output/thesis_report.docx")
print("Report saved to:", report_path)
```
