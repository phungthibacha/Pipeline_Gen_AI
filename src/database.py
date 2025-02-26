import psycopg2
from psycopg2 import sql
from data_contract import Sales
import streamlit as st
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# PostgreSQL database configuration
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Function to save validated data in PostgreSQL
def save_to_postgres(data: Sales):
    """
    This function is used to save data into postgres
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        #cursor will create a connection with database
        cursor = conn.cursor()
        
        # Inserting data into the sales table
        insert_query = sql.SQL(
            "INSERT INTO sales (email, date_time, value, product_qty, product_category) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            data.email,
            data.date_time,
            data.value,
            data.product_qty,
            data.product_category.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Data successfully saved to the database!")
    except Exception as e:
        st.error(f"Error saving to database: {e}")