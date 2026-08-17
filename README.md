# SkillLab: Python & SQL Lab Solutions

A repository containing comprehensive solutions for Python programming and SQL relational database management challenges.

---

## 📁 Repository Structure

```
SkillLab/
│
├── Part_A/
│   ├── card_game.py       # Multi-player card game simulator implementation
│   └── README.md          # Technical documentation for Part A
│
└── Part_B/
    ├── employee_database.sql  # SQL schema DDL, DML, and query challenges
    ├── main.py                # Python SQLite executor with ASCII table formatting
    └── README.md              # Technical documentation for Part B
```

---

## 🃏 Part A: Multi-Player Card Game Simulator

A round-based multi-player card game engine built in Python.

### Technical Highlights
- **Deck Creation**: Generated using Python **list comprehension** (`[f"{rank} of {suit}" for suit in suits for rank in ranks]`).
- **Deck Shuffling & Fair Distribution**: Shuffles deck using `random.shuffle()` and divides cards evenly among $N$ players ($1 \le N \le 52$). Extra cards are set aside fairly if non-divisible.
- **Round Mechanics**: Simulates rounds by picking random cards from each player's active hand.
- **Input Validation**: Robust user input handling for player count and round winner selections.
- **Score Tracking**: Tracks cumulative round victories and identifies single or tied winners.

### Execution
```bash
python Part_A/card_game.py
```

---

## 🗄️ Part B: Employee Relational Database & SQL Queries

An employee database system implemented in ANSI SQL and automated using SQLite via Python.

### Technical Highlights
- **Relational Schema**:
  - `Department`: `department_id` (PRIMARY KEY), `department_name` (UNIQUE)
  - `Employee`: `emp_id` (PRIMARY KEY), `emp_name`, `department_id` (FOREIGN KEY), `department_name`, `job_title`, `salary`
- **SQL Query Challenges**:
  1. Select all records (`SELECT * FROM Employee`)
  2. Distinct department names (`SELECT DISTINCT`)
  3. Salary threshold filter (`WHERE salary > 50000`)
  4. Department filter (`WHERE department_name = 'IT'`)
  5. Salary range (`WHERE salary BETWEEN 45000 AND 75000`)
  6. Set membership (`WHERE department_name IN (...)`)
  7. Sorting results (`ORDER BY salary DESC`)
  8. Compound logical filters (`AND`, `OR`, `NOT`)
- **ASCII Table Formatter**: Custom formatted tabular output generator in `main.py`.

### Execution
Run via Python (SQLite in-memory executor):
```bash
python Part_B/main.py
```

Or execute `Part_B/employee_database.sql` directly using any SQL client (MySQL, PostgreSQL, SQLite Browser, DBeaver).

---

## ⚙️ Prerequisites

- **Python 3.7+** (Uses standard libraries: `random`, `sqlite3`, `sys`, `os`)
- No third-party package dependencies required.

---

## 📄 License

This repository is maintained for lab solutions and educational reference.
