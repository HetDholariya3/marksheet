# 🎓 Student Marksheet Management System

A desktop GUI application built with Python (Tkinter) and MySQL to manage student records, including subject-wise marks, and generate result summaries with pass/fail status and percentage.

## 🚀 Features

- ✅ Add new student records with validation
- ✏️ Update existing records by student name
- ❌ Delete student records
- 📋 Show all stored records
- 📊 Generate result (Pass/Fail + Percentage)
- 🔐 Validates:
  - Enrollment number (14-digit)
  - Semester (1 to 6)
  - Marks range (0-100)

## 🛠️ Tech Stack

- **Frontend**: Python with Tkinter
- **Backend**: MySQL
- **Connector**: `mysql-connector-python`

---

## 🗃️ Database Setup

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
