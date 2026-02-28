from sales_analyzer import DataLoader, DataCleaner, SalesAnalyzer, Visualizer, ReportGenerator

def main():

    file_path = "data/raw/sales_data.csv"

    loader = DataLoader(file_path)
    df = loader.load_data()

    cleaner = DataCleaner(df)
    df = cleaner.clean()

    analyzer = SalesAnalyzer(df)
    visualizer = Visualizer(df)
    reporter = ReportGenerator(df, analyzer)

    while True:
        print("\nSALES ANALYSIS DASHBOARD")
        print("1. Show Basic Stats")
        print("2. Analyze Category Sales")
        print("3. Show Monthly Trends")
        print("4. Generate Visualizations")
        print("5. Generate Reports")
        print("6. Run Full Analysis")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            stats = analyzer.basic_stats()

            print("\n📊 SALES SUMMARY")
            print("="*30)
            print(f"Total Sales: ₹{stats['Total Sales']}")
            print(f"Average Order Value: ₹{stats['Average Order Value']}")
            print(f"Total Orders: {stats['Total Orders']}")
            print(f"Unique Customers: {stats['Unique Customers']}")
            print(f"Unique Products: {stats['Unique Products']}")

        elif choice == "2":
            print(analyzer.sales_by_category())

        elif choice == "3":
            print(analyzer.monthly_trends())

        elif choice == "4":
            visualizer.monthly_trend_plot()
            visualizer.category_bar_chart()
            visualizer.order_distribution()
            print("All visualizations generated.")

        elif choice == "5":
            reporter.generate_excel_report()
            reporter.generate_text_summary()
            print("Reports generated.")

        elif choice == "6":
            stats = analyzer.basic_stats()

            print("\n📊 SALES SUMMARY")
            print("="*30)
            print(f"Total Sales: ₹{stats['Total Sales']}")
            print(f"Average Order Value: ₹{stats['Average Order Value']}")
            print(f"Total Orders: {stats['Total Orders']}")
            print(f"Unique Customers: {stats['Unique Customers']}")
            print(f"Unique Products: {stats['Unique Products']}")

            visualizer.monthly_trend_plot()
            visualizer.category_bar_chart()
            visualizer.order_distribution()

            reporter.generate_excel_report()
            reporter.generate_text_summary()

            print("\n✅ Full analysis complete. All reports and visualizations generated.")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()