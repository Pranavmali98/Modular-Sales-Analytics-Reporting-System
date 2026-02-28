import pandas as pd

class SalesAnalyzer:

    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return {
    "Total Sales": round(float(self.df['total_amount'].sum()), 2),
    "Average Order Value": round(float(self.df['total_amount'].mean()), 2),
    "Total Orders": int(len(self.df)),
    "Unique Customers": int(self.df['customer_id'].nunique()),
    "Unique Products": int(self.df['product_id'].nunique())
    }

    def sales_by_category(self):
        return self.df.groupby('category')['total_amount'].sum().sort_values(ascending=False)

    def top_products(self, n=10):
        return self.df.groupby('product_id')['total_amount'].sum().sort_values(ascending=False).head(n)

    def monthly_trends(self):
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        monthly = self.df.groupby('month')['total_amount'].sum()
        return monthly

    def monthly_growth(self):
        monthly = self.monthly_trends()
        return monthly.pct_change() * 100

    def moving_average_forecast(self, window=3):
        monthly = self.monthly_trends()
        return monthly.rolling(window=window).mean()