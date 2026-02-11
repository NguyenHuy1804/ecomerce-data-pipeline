# Ecommerce Batch Data Pipeline

## Overview
This project implements a batch ETL pipeline using Python and PostgreSQL.

## Architecture
CSV → Transform → Star Schema → PostgreSQL

## Technologies
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker

## Data Warehouse Design
Star Schema:
- dim_customers
- dim_products
- dim_date
- fact_orders
