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
