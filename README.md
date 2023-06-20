# Quiz application

A Quiz is made of Questions. Every Question is related to a topic, and has a difficulty rank number (1 the most, 
3 the least difficult). Every Question has a content and a list of Responses. Every Response has a content text 
and a boolean (correct).

Used IDE: IntelliJ IDEA Community Edition 2023.1.1.

### Project setup

Installed psycopg2.

### Structure and functionalities

Database directory: contains files for db connection and inserting tables to db.  
Model directory: contains models to insert data to db.  
quiz_app.py: for initializing objects and calling methods.  
