# Part B: Employee Relational Database & SQL Queries

## Overview
This component creates an `Employee` relational database table with constraints (`PRIMARY KEY`, `FOREIGN KEY`, data types), inserts employee records, and executes fundamental SQL queries to satisfy specified business challenges.

## SQL Schema & Constraints
- **`Department` Table**: Holds unique department records with `department_id` as `PRIMARY KEY`.
- **`Employee` Table**: Holds employee details with `emp_id` as `PRIMARY KEY` and `department_id` referencing `Department(department_id)` as `FOREIGN KEY`.

## SQL Query Challenges Included
1. **All Records**: `SELECT * FROM Employee`
2. **Distinct Departments**: `SELECT DISTINCT department_name FROM Employee`
3. **Salary Filter**: `SELECT * FROM Employee WHERE salary > 50000`
4. **Department Filter**: `SELECT * FROM Employee WHERE department_name = 'IT'`
5. **Salary Range**: `SELECT * FROM Employee WHERE salary BETWEEN 45000 AND 75000`
6. **In Operator**: `SELECT * FROM Employee WHERE department_name IN ('IT', 'Finance', 'HR')`
7. **Sorting**: `SELECT * FROM Employee ORDER BY salary DESC`
8. **Logical Operators**: `SELECT * FROM Employee WHERE department_name = 'IT' AND salary > 50000 OR NOT department_name = 'HR'`

## How to Run
Run the Python script to execute the SQL queries against an in-memory SQLite database:
```bash
python Part_B/main.py
```
Or execute `Part_B/employee_database.sql` directly in any SQL database tool (MySQL, PostgreSQL, SQLite, SQLite Browser, etc.).
