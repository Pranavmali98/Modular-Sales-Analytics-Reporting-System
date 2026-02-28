import numpy as np

class DataCleaner:

    def __init__(self, df):
        self.df = df

    def clean(self):
        self.remove_duplicates()
        self.handle_missing()
        self.fix_data_types()
        self.remove_invalid_rows()
        return self.df

    def remove_duplicates(self):
        self.df = self.df.drop_duplicates()

    def handle_missing(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        categorical_cols = self.df.select_dtypes(include=['object']).columns

        for col in numeric_cols:
            self.df[col].fillna(self.df[col].median(), inplace=True)

        for col in categorical_cols:
            self.df[col].fillna(self.df[col].mode()[0], inplace=True)

    def fix_data_types(self):
        self.df['quantity'] = self.df['quantity'].astype(int)
        self.df['total_amount'] = self.df['total_amount'].astype(float)

    def remove_invalid_rows(self):
        self.df = self.df[self.df['quantity'] > 0]
        self.df = self.df[self.df['total_amount'] > 0]