import pandas as pd

class DataLoader:
    REQUIRED_COLUMNS = [
        'order_id',
        'customer_id',
        'product_id',
        'category',
        'quantity',
        'total_amount',
        'order_date'
    ]

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            if self.file_path.endswith('.csv'):
                df = pd.read_csv(self.file_path)
            else:
                df = pd.read_excel(self.file_path)

            if df.empty:
                raise Exception("Dataset is empty. Please check the CSV file.")

            self.validate_columns(df)
            df['order_date'] = pd.to_datetime(df['order_date'])

            print(f"Data loaded successfully. Shape: {df.shape}")
            return df

        except pd.errors.EmptyDataError:
            raise Exception("The file exists but contains no data.")

        except FileNotFoundError:
            raise Exception("File not found. Check the file path.")

        except Exception as e:
            raise Exception(f"Error loading data: {e}")

    def validate_columns(self, df):
        missing = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]
        if missing:
            raise Exception(f"Missing required columns: {missing}")