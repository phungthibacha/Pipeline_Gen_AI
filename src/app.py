import streamlit as st
from data_contract import Sales, ProductEnum
from datetime import datetime, time
from pydantic import ValidationError
from database import save_to_postgres

def main():
    st.title("ZapFlow CRM and Sales System")
    email = st.text_input("Buyer Email")
    purchase_date = st.date_input("Purchase Date", datetime.now())
    purchase_time = st.time_input("Time to Buy", value=time(9,0))
    value = st.number_input("Sale Value", min_value = 0.0, format="%.2f")
    product_qty = st.number_input("Quantity of Products", min_value=1, step=1)
    product_category = st.selectbox("Product", options = [e.value for e in ProductEnum])

    if st.button("Save"):
        try:
            # Combine purchase date and time 
            date_time = datetime.combine(purchase_date, purchase_time)
            # Validating data with Pydantic
            sales = Sales(
                email = email, 
                date_time = date_time,
                value = value, 
                product_qty = product_qty, 
                product_category = product_category
                )
            st.write(sales)
            save_to_postgres(sales)
            st.success("Data validated and saved successfully!")
        except ValidationError as e:
            st.error(f"Data validation error: {e}")
        except Exception as e:
            st.error(f"Error saving data: {e}")

if __name__=="__main__":
    main()