#Student Marksheet Management System

This project is a GUI-based Python application using Tkinter and MySQL to manage student marksheets.

## Features
- Add student records
- Update and delete existing records
- Show all student data
- Display result with pass/fail status and percentage

## Technologies Used
- Python (Tkinter)
- MySQL
- MySQL Connector

1. **Create MySQL Database** (or import directly):
    - Create a database called `marksheet`
    - Use this table structure:

```sql
CREATE DATABASE marksheet;

USE marksheet;

CREATE TABLE results (
    fname VARCHAR(50),
    lname VARCHAR(50),
    enrollment BIGINT,
    division VARCHAR(10),
    semester INT,
    ds FLOAT,
    laravel FLOAT,
    c_language FLOAT,
    java FLOAT,
    python FLOAT
);
