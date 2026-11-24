# OOP Supermarket Checkout Simulation

A Python project (COMP1811 – Paradigms of Programming, Logbook Task 1) that simulates customers moving through supermarket checkout lanes, built to practise **object-oriented programming** concepts such as classes, inheritance and method overriding.

## Overview

The simulation models:

- **Customers** – generated with a random ID and a random number of basket items (1–30).
- **Checkout lanes** – a base `Lane` class with two specialised subclasses:
  - `Service_lane` (staffed cashier lane)
  - `Regular_lane` / self-checkout lane
- **Processing time** – based on the number of items (e.g. 4s per item at self-checkout, 6s per item with a cashier).
- **Arriving customers** – new customers join the queue over time.
- **GUI** – a basic Tkinter interface with buttons to start/stop the simulation, show customer basket details and exit.

## OOP Concepts Demonstrated

- Classes and objects (`Customers`, `Lane`, `MyGUI`)
- Inheritance (`Service_lane(Lane)`, `Regular_lane(Lane)`, `Basket(Customers)`)
- Method overriding (`add_customer`, `process_customer`, `display`)
- Encapsulation of lane state (capacity, queue of customers)

## Project Files

| File | Description |
|------|-------------|
| `tkinter_final.py` | Latest version – simulation with a Tkinter GUI |
| `final.py` | Console version of the simulation with customer and lane classes |
| `lanes class.py` | Lane class hierarchy (`Lane`, `Service_lane`, `Regular_lane`) |
| `nkk.py`, `sds.py`, `asd.py` | Earlier prototypes of the customer/checkout logic |
| `testing.py`, `testing testing.py`, `testin testin testing.py`, `time testing.py`, `tkinter test.py` | Scratch/test scripts used during development |
| `main.py` | Default PyCharm sample script |

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)

No third-party packages are required.

## Running

```bash
# GUI version
python tkinter_final.py

# Console version
python final.py
```

## Author

> All code in this project was written by the author without the use of AI tools.

Abhishekh Rajan – COMP1811 Logbook Task 1
