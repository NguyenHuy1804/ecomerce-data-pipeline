import pandas as pd

def transform(df):

    df = df.dropna(subset=['CustomerID']).copy()

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    df = df[df['Quantity'] > 0].copy()
    df = df[df['UnitPrice'] > 0].copy()

    df = df.drop_duplicates().copy()

    return df


def create_dimensions(df):

    # ----- DIM CUSTOMERS -----
    dim_customers = df[['CustomerID']].drop_duplicates().reset_index(drop=True)
    dim_customers['customer_id'] = dim_customers.index + 1

    df = df.merge(dim_customers, on='CustomerID')

    # ----- DIM PRODUCTS -----
    dim_products = df[['StockCode']].drop_duplicates().reset_index(drop=True)
    dim_products['product_id'] = dim_products.index + 1

    df = df.merge(dim_products, on='StockCode')

    # ----- DIM DATE -----
    dim_date = df[['InvoiceDate']].drop_duplicates().reset_index(drop=True)
    dim_date['date_id'] = dim_date.index + 1
    dim_date['day'] = dim_date['InvoiceDate'].dt.day
    dim_date['month'] = dim_date['InvoiceDate'].dt.month
    dim_date['year'] = dim_date['InvoiceDate'].dt.year

    df = df.merge(dim_date, on='InvoiceDate')

    # ----- FACT TABLE -----
    fact_orders = df[['InvoiceNo', 'customer_id', 'product_id', 'date_id', 'Quantity']]
    fact_orders['total_amount'] = df['Quantity'] * df['UnitPrice']

    return dim_customers[['customer_id', 'CustomerID']], \
           dim_products[['product_id', 'StockCode']], \
           dim_date[['date_id', 'InvoiceDate', 'day', 'month', 'year']], \
           fact_orders

