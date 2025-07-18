# Quadratic Equation Solver

This is a simple Python script that solves quadratic equations of the form ax² + bx + c = 0

It also handles special cases where:
- `a = 0`, reducing the equation to a linear form: `bx + c = 0`
- The equation has no real solutions
- The equation has infinitely many solutions

## 📌 Features

- Solves quadratic equations using the discriminant (Δ = b² - 4ac)
- Handles linear equations if a = 0
- Detects and reports:
  - Two real solutions
  - One real solution (when Δ = 0)
  - No real solution (when Δ < 0)
  - Infinite or no solution in degenerate linear cases
- Interactive user input via command-line

## 🧪 Example

This program can calculate the solutions of the quadratic equation for you.
Please enter the requested values based on ax^2 + bx + c.
a: 1
b: -3
c: 2
2 answer found , x=2.0,1.0

## 🚀 How to Run

Make sure you have Python installed (version 3+), then run the script:

bash

python3 quadratic_solver.py

## 📂 Files

quadratic_solver.py – main Python script

.gitignore – ignores Python cache, virtual environments, VS Code settings

README.md – you're reading it :)


Author:Abolfazl Ghorbani











