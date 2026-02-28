import matplotlib.pyplot as plt
import os

class Visualizer:

    def __init__(self, df):
        self.df = df
        os.makedirs("data/reports", exist_ok=True)

    def monthly_trend_plot(self):
        monthly = self.df.groupby(self.df['order_date'].dt.to_period('M'))['total_amount'].sum()

        plt.figure(figsize=(10,6))
        monthly.plot()
        plt.title("Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Sales")
        plt.grid(True)
        plt.savefig("data/reports/monthly_trend.png")
        plt.close()

    def category_bar_chart(self):
        category = self.df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

        plt.figure(figsize=(10,6))
        category.plot(kind='bar')
        plt.title("Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.savefig("data/reports/category_sales.png")
        plt.close()

    def order_distribution(self):
        plt.figure(figsize=(10,6))
        plt.hist(self.df['total_amount'], bins=30)
        plt.title("Order Value Distribution")
        plt.xlabel("Order Value")
        plt.ylabel("Frequency")
        plt.savefig("data/reports/order_distribution.png")
        plt.close()