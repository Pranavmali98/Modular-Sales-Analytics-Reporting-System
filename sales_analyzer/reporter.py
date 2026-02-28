import pandas as pd

class ReportGenerator:

    def __init__(self, df, analyzer):
        self.df = df
        self.analyzer = analyzer

    def generate_excel_report(self):
        with pd.ExcelWriter("data/reports/sales_report.xlsx") as writer:
            pd.DataFrame([self.analyzer.basic_stats()]).to_excel(writer, sheet_name="Summary", index=False)
            self.analyzer.sales_by_category().to_excel(writer, sheet_name="Category Sales")
            self.analyzer.monthly_trends().to_excel(writer, sheet_name="Monthly Trends")
            self.df.head(1000).to_excel(writer, sheet_name="Sample Data", index=False)

    def generate_text_summary(self):
        stats = self.analyzer.basic_stats()

        with open("data/reports/executive_summary.txt", "w") as f:
            f.write("SALES EXECUTIVE SUMMARY\n")
            f.write("="*30 + "\n")
            for key, value in stats.items():
                f.write(f"{key}: {value}\n")