CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    date_time TIMESTAMP NOT NULL,
    value NUMERIC NOT NULL,
    product_qty INTEGER NOT NULL,
    product_category VARCHAR(50) NOT NULL
)