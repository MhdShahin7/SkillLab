import sqlite3
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


def print_table(cursor, title):
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    
    print("\n" + "=" * 75)
    print(f"  {title}")
    print("=" * 75)

    if not rows:
        print("  (No records found)")
        return

    widths = [len(col) for col in columns]
    for row in rows:
        for i, val in enumerate(row):
            widths[i] = max(widths[i], len(str(val)))

    header_str = " | ".join(f"{col:{widths[i]}}" for i, col in enumerate(columns))
    separator_str = "-+-".join("-" * widths[i] for i in range(len(columns)))
    
    print(header_str)
    print(separator_str)

    for row in rows:
        row_str = " | ".join(f"{str(val):{widths[i]}}" for i, col in enumerate(row))
        print(row_str)
    print(f"Total records returned: {len(rows)}")


def run_database_challenge():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    sql_file_path = os.path.join(os.path.dirname(__file__), "employee_database.sql")

    with open(sql_file_path, "r", encoding="utf-8") as f:
        sql_content = f.read()

    cursor.executescript("""
    CREATE TABLE Department (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE Employee (
        emp_id INTEGER PRIMARY KEY,
        emp_name TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        department_name TEXT NOT NULL,
        job_title TEXT NOT NULL,
        salary REAL NOT NULL,
        FOREIGN KEY (department_id) REFERENCES Department(department_id)
    );

    INSERT INTO Department (department_id, department_name) VALUES
    (101, 'IT'), (102, 'HR'), (103, 'Finance'), (104, 'Marketing'), (105, 'Sales');

    INSERT INTO Employee (emp_id, emp_name, department_id, department_name, job_title, salary) VALUES
    (1, 'Rahul Sharma', 101, 'IT', 'Software Engineer', 65000),
    (2, 'Priya Patel', 102, 'HR', 'HR Executive', 45000),
    (3, 'Amit Kumar', 103, 'Finance', 'Financial Analyst', 75000),
    (4, 'Sneha Reddy', 101, 'IT', 'Senior Developer', 82000),
    (5, 'Vikram Singh', 104, 'Marketing', 'Marketing Specialist', 48000),
    (6, 'Ananya Roy', 105, 'Sales', 'Sales Manager', 52000),
    (7, 'Deepak Verma', 101, 'IT', 'Junior Developer', 40000),
    (8, 'Neha Gupta', 102, 'HR', 'HR Manager', 58000),
    (9, 'Rajesh Iyer', 103, 'Finance', 'Finance Director', 90000),
    (10, 'Kavita Joshi', 104, 'Marketing', 'Content Writer', 35000);
    """)

    print("✅ Database initialized and employee records inserted successfully.")

    cursor.execute("SELECT * FROM Employee;")
    print_table(cursor, "Query 1: Display All Employee Records")

    cursor.execute("SELECT DISTINCT department_name FROM Employee;")
    print_table(cursor, "Query 2: Display Unique Department Names")

    cursor.execute("SELECT * FROM Employee WHERE salary > 50000;")
    print_table(cursor, "Query 3: Employees Earning More Than ₹50,000")

    cursor.execute("SELECT * FROM Employee WHERE department_name = 'IT';")
    print_table(cursor, "Query 4: Employees in IT Department")

    cursor.execute("SELECT * FROM Employee WHERE salary BETWEEN 45000 AND 75000;")
    print_table(cursor, "Query 5: Employees Earning Between ₹45,000 and ₹75,000")

    cursor.execute("SELECT * FROM Employee WHERE department_name IN ('IT', 'Finance', 'HR');")
    print_table(cursor, "Query 6: Employees in Selected Departments (IT, Finance, HR)")

    cursor.execute("SELECT * FROM Employee ORDER BY salary DESC;")
    print_table(cursor, "Query 7: Employees Sorted by Salary Descending")

    cursor.execute("SELECT * FROM Employee WHERE department_name = 'IT' AND salary > 50000 OR NOT department_name = 'HR';")
    print_table(cursor, "Query 8: Multiple Conditions with AND, OR, NOT")

    conn.close()


if __name__ == "__main__":
    run_database_challenge()
