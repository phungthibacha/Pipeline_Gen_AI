## Introduction
ZapFlow's CRM and Sales System is an application developed to manage and validate sales in a simple and efficient way. The system consists of an interactive frontend developed with Streamlit, data validation with Pydantic, and integration with a PostgreSQL database using Psycopg2.

## Sequence Diagram
The following diagram illustrates the flow of interaction between the user, the web system, data validation and the database.


## Technologies Used
Streamlit
Description: Streamlit is an open-source Python library that lets you quickly and easily create interactive web applications. Primarily used for building dashboards and data interfaces, Streamlit is ideal for rapid prototyping and data visualization without requiring advanced web development knowledge.
Project Usage: Used to build the frontend of the application, allowing users to interactively enter sales data and view the results directly in the interface.
Pydantic
Description: Pydantic is a data validation library that uses Python class-based models to ensure that input data is in the correct format. It is widely used for data validation and serialization, ensuring integrity and consistency.
Project Usage: Pydantic is used to validate data entered by users on the frontend, ensuring that the information is correct before being processed and saved to the database.
Psycopg2
Description: Psycopg2 is a library that allows interaction with PostgreSQL databases directly through Python, facilitating the execution of SQL commands and the management of connections.
Project Usage: Used to connect the application to the PostgreSQL database, execute SQL commands, and save validated data.
SQLAlchemy (Opcional)
Description: SQLAlchemy is a powerful SQL toolkit and ORM (Object-Relational Mapping) library for Python. It allows you to interact with relational databases more intuitively, using Python objects instead of SQL commands directly.
Usage in the Project: SQLAlchemy could be used to manage the connection to the PostgreSQL database and facilitate CRUD operations (optional, not implemented in the current example).
MkDocs
Description: MkDocs is a static Python documentation tool that allows you to create documentation sites in a simple and structured way. It is especially useful for projects that need clear and accessible documentation for developers and users.
Project Usage: MkDocs is used to generate system documentation, detailing how the project was structured, the functionalities developed, and how the system should be maintained and updated.
Project Structure
Module Division
The project is divided into modules to better organize development and facilitate future maintenance. The following are the main modules of the project:

Frontend (app.py):

Responsible for the user interface where sales data is entered and displayed.
Developed with Streamlit to provide simple and user-friendly interaction.
Contract ( contrato.py):

Define data validation rules using Pydantic.
Ensures that the data entered into the frontend is in the correct format and complies with the rules established by the system.
Database ( database.py):

Manages the connection and operations with the PostgreSQL database using Psycopg2.
It facilitates interaction with the bank without the need to write SQL directly.
## Steps for Configuration and Execution
1. Create the Repository
Step: Start a new repository on GitHub or GitLab to version the project.
Command:
git init
2. Choose Python Version to 3.12.1
Use this pyenvto manage and set the correct Python version:
pyenv install 3.12.1
pyenv local 3.12.1
3. Create a Virtual Environment
Step: Create a virtual environment to isolate project dependencies.
Command:
python3.12 -m venv .venv
4. Enter the Virtual Environment
Command:
Windows:
.venv\Scripts\activate
Linux/Mac:
source .venv/bin/activate
5. Install Dependencies
Install the required packages:
pip install -r requirements.txt
6. Run the Frontend
Command to run the frontend with Streamlit:
streamlit run app.py
7. Configure PostgreSQL
Create the database and the required table:
CREATE DATABASE crm_vendas;
CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    data TIMESTAMP NOT NULL,
    valor NUMERIC NOT NULL,
    quantidade INTEGER NOT NULL,
    produto VARCHAR(50) NOT NULL
);
8. Create the Connection to PostgreSQL
The connection is managed in the module database.pyusing psycopg2.
Conclusion
This README serves as a guide to setting up, understanding, and running ZapFlow's CRM and Sales System. The project combines a series of modern technologies to provide an efficient and easy-to-use sales management solution. With well-defined modules and clear documentation, the system is prepared to evolve and adapt to the needs of users.

## Requirements Document with Validations - ZapFlow CRM and Sales System
## Aim
The purpose of this document is to define the functional requirements and validations needed to develop the frontend of ZapFlow's CRM and Sales System, developed with Streamlit. The system aims to capture information about sales made, validate it and display it on the screen.

Here is the diagram in Mermaid that describes the data flow from user input on the frontend to data validation and saving to the database if approved.


## Diagram Description:
User Types in Frontend:

The user enters the necessary data into the system frontend.
Data Contract Validation:

The data entered is validated using the Pydantic model (data contract) to ensure it is in the correct format and within the specified rules.
Valid Data:

If the data is valid, it is sent to the database and saved.
Invalid Data:

If the data does not meet the validation criteria, an error message is generated and displayed on the frontend.
Save to Database:

After validation, the data is persisted in the database.
Message Display:

Displays a success message when data is saved correctly, or an error message when validation fails.
This diagram shows the complete flow from data entry to data saving, detailing the validation process essential to maintaining system integrity.

Functional Requirements and Validations
System Title

Description: The system should display the title "ZapFlow CRM and Sales System - Simple Frontend" at the top of the page.
Justification: Clearly identify the system and its purpose for the user.
Data Entry Fields

The system must provide fields for entering sales data. Each field must be clearly identified and must accept the correct input type as described below, with the respective validations.
Field Details and Validations
Seller Email

Description: Text field for entering the seller's email.
Input Type: text_input (String)
Expected Validation:
It must be a valid email in standard format (ex: vendedor@exemplo.com).
Check if the field is not empty.
Usage Example: The user enters a valid email, such as vendedor@exemplo.com.
Purchase Date

Description: Field to select the date on which the sale was made.
Input Type: date_input (Data)
Default Value: The current date ( datetime.now()).
Expected Validation:
The date must be within the allowed range: between 01/09/2024and 12/09/2024.
Do not allow dates outside the specified range.
Usage Example: The user selects a date as 05/09/2024.
Time to Buy

Description: Field to select the time the sale was made.
Entry Type: time_input (Hour)
Default Value: 09:00 (default start time).
Expected Validation:
The time must be entered within the range of 09:00 to 17:00.
Usage Example: The user selects 10:30.
Sale Value

Description: Numeric field to enter the monetary value of the sale made.
Input Type: number_input (Float)
Minimum Value: 0.0 (negative values ​​are not allowed).
Format: Decimal with two places ( format="%.2f").
Expected Validation:
Must be a positive number greater than zero.
It must be in the proper monetary format with two decimal places.
Usage Example: The user enters 1500.00.
Quantity of Products

Description: Numeric field to enter the quantity of products sold.
Input Type: number_input (Integer)
Minimum Value: 1 (minimum quantity allowed).
Step: 1 unit increment per adjustment.
Expected Validation:
Must be a positive integer.
It must not be zero or negative.
Usage Example: The user enters 3.
Product

Description: Selection field to choose the product sold.
Input Type: selectbox (Selection)
Available Options:
"ZapFlow com Gemini"
"ZapFlow com chatGPT"
"ZapFlow com Llama3.0"
Expected Validation:
The selected product must be one of the valid options.
Do not allow selection of products outside of the listed options.
Usage Example: User selects "ZapFlow with chatGPT".
Submit Button

Description: A button to save and display data entered on the screen.
Button Label: "Save"
Behavior: When clicked, the system should capture the data entered in the fields, validate the entries and display them on the screen if all fields are correct.
Data Display

Description: After submission, the system should display the captured data on the screen.
Display Formats:
Seller Email: Displays the email entered.
Purchase Date and Time: Displays the combined date and time as yyyy-mm-dd hh:mm:ss.
Sales Value: Displays the value formatted as currency, e.g.: R$ 1500.00.
Product Quantity: Displays the quantity entered.
Product: Displays the name of the selected product.
Notes
This system captures and validates data before displaying it, ensuring that all entries are correct according to defined rules.
In future versions, the system may be integrated with a backend for data persistence and advanced analysis and reporting features.
Future Objective
Integrate advanced validations to enforce data integrity.
Connect the system to a database to store sales and generate reports.
Add additional checks for required fields and duplicate data.
