import pandas as pd
from sales_analyzer.analyzer import SalesAnalyzer

def test_basic_stats():
    data = {
        'order_id':[1,2],
        'customer_id':[101,102],
        'product_id':[201,202],
        'category':['A','B'],
        'quantity':[1,2],
        'total_amount':[100,200],
        'order_date':['2024-01-01','2024-01-02']
    }

    df = pd.DataFrame(data)
    df['order_date'] = pd.to_datetime(df['order_date'])

    analyzer = SalesAnalyzer(df)
    stats = analyzer.basic_stats()

    assert stats["Total Sales"] == 300