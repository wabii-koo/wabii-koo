Simulated Annealing in Python
Overview

This Python script implements Simulated Annealing to minimize the function:

f(x) = x^2


It searches for the value of x that produces the smallest output.

Requirements

Python 3.x

NumPy (pip install numpy)

How to Run
python simulated_annealing.py


The program outputs the best solution and its cost:

Best Solution: <value>
Best Cost: <value>

How It Works

Starts with a random solution.

Explores neighbors with small random changes.

Accepts better solutions, and sometimes worse solutions to escape local minima.

Gradually reduces temperature until the search stops.

Tracks the best solution found.
