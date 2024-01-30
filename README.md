# API-check-sql-injection-ORM-method
Built an API using Flask to receive a JSON payload via POST request for checking the input string for any SQL injection characters and in result it return a JSON response stating that given input is sanitized or unsanitized. Wrote unit test cases as well using pytest.

In this project i have used ORM (Object relational mapping) tool SQLAlchemy to interact with databases using python objects instead of using raw SQL queries. firstly i have defined a fun for checking if input contains any SQL injection characters by comparing with potential SQL injections characters. After that created another fun for handling post request. it retrieves the JSON data from the request and then check for empty input and then check for SQL injection charcters. used SQLAlchemy to define a model `inputData` and interact with database using object instead of raw SQL queries.

For this project i have created one virtual env and inside that i have installed Flask ,Flask-SQLAlchemy, pytest for running and testing this project successfully without having anyt dependency from system environment.

To run the API on local use command -- python app.py or flask run 
To run the unit test case use command -- pytest test_app.py
