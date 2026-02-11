from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:1234@localhost:5432/postgres"
)

def load_table(df, table_name):
    print(f"Loading {table_name}...")
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"{table_name} loaded!")
