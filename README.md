# CIS 41A — Python Programming

Python coursework from De Anza College, including short programming exercises and a command-line **De Anza Food Court ordering system**. The files show a progression from input validation and functions to modules, classes, inheritance, file output, and unit testing.

[![Python](https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white)](#repository-guide)
[![Featured](https://img.shields.io/badge/featured-food%20court%20ordering%20system-ff7f50?style=flat-square)](#featured-project-de-anza-food-court)

## Course context

De Anza's CIS 41A introduces Python data types and collections, control flow, functions, modules, object-oriented programming, file handling, regular expressions, and exceptions. This repository contains selected coursework, rather than an implementation of every topic in the course.

## Featured project: De Anza Food Court

The food court project models a fictional ordering workflow:

- Choose from five burgers and enter positive quantities.
- Identify the customer as a student or staff member.
- Calculate item totals and apply the project's tax rules: 0% for students and 9% for staff.
- Print an itemized receipt and save a timestamped text receipt.
- Start another order in the same session.
- Add, inspect, update, and remove order items through methods on the `Order` class.

These prices and tax rules belong to the exercise; they are not current campus dining information. The interactive main program handles ordering and checkout. CRUD methods and a separate demonstration function are available in the source, but the main loop does not expose a CRUD menu.

## Repository guide

| Path | Contents |
| --- | --- |
| [FINAL/](FINAL/) | Object-oriented food court project, tests, sample receipts, and class diagram |
| [Midterm1.py](Midterm1.py) | Earlier food court implementation organized around functions |
| [C6E4/](C6E4/) | Payroll program split into input, calculation, and output modules |
| `C2E*.py`–`C5E*.py` | Payroll, circle graphics, strings, digit sums, validation, and functions |
| [C6E1.py](C6E1.py), [C6E2.py](C6E2.py) | Friends collections using lists and dictionaries |
| [C9EC.py](C9EC.py) | A small `Bug` class with movement and direction changes |
| [demo0.py](demo0.py) | Graphics demonstration |

Within `FINAL/`, `main.py` controls the console workflow, `order.py` manages orders and receipts, `person.py` defines customer classes, and `food_item.py` defines the burger class hierarchy. The order implementation currently stores menu prices and quantities in dictionaries.

## Run

Use Python 3. The final project uses the standard library and local modules; no pip packages are needed.

```sh
git clone https://github.com/kjw0716/CIS41A.git
cd CIS41A/FINAL
python main.py
```

Choose items `1`–`5`, enter quantities, and enter `6` to finish selecting items. Then choose `0` for student or `1` for staff. Receipts are written to the current working directory. Choosing `6` before adding anything exits the program.

Run the existing test suite from `FINAL/`:

```sh
python -m unittest -v test_order
```

The 22 existing tests cover burger and customer classes, validation, order operations, and integration scenarios. They passed with Python 3.13 during documentation verification.

Other exercises can be run individually, for example `python C5E1.py` from the repository root. `C2E2.py`, `C2E3.py`, and `demo0.py` additionally require the `ezgraphics` module and a graphical desktop. That dependency is not included in this repository.

## References and attribution

- [De Anza CIS 41A course description](https://daweb2.deanza.edu/schedule/class-details.html?crn=46054&q=S&y=2026) — general course background; not a claim about the original section or term.
- Implementation details are documented from the source files in this repository. The original Canvas project brief was not available in the accessible course list.
- Source headers credit Jackie Wang and the **Python Enjoyers** team. Existing attribution is retained in the project files.
