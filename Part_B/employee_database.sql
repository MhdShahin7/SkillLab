CREATE TABLE IF NOT EXISTS Department (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Employee (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    department_name TEXT NOT NULL,
    job_title TEXT NOT NULL,
    salary REAL NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

INSERT INTO Department (department_id, department_name) VALUES
(101, 'IT'),
(102, 'HR'),
(103, 'Finance'),
(104, 'Marketing'),
(105, 'Sales');

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

SELECT * FROM Employee;

SELECT DISTINCT department_name FROM Employee;

SELECT * FROM Employee 
WHERE salary > 50000;

SELECT * FROM Employee 
WHERE department_name = 'IT';

SELECT * FROM Employee 
WHERE salary BETWEEN 45000 AND 75000;

SELECT * FROM Employee 
WHERE department_name IN ('IT', 'Finance', 'HR');

SELECT * FROM Employee 
ORDER BY salary DESC;

SELECT * FROM Employee 
WHERE department_name = 'IT' AND salary > 50000 
   OR NOT department_name = 'HR';
