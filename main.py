from src.extract import extract
from src.transform import transform, create_dimensions
from src.load import load_table

df = extract()
df_clean = transform(df)

dim_customers, dim_products, dim_date, fact_orders = create_dimensions(df_clean)

load_table(dim_customers, "dim_customers")
load_table(dim_products, "dim_products")
load_table(dim_date, "dim_date")
load_table(fact_orders, "fact_orders")
