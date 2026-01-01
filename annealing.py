import numpy as np
import random
import math

def objective_function(x):
    return x**2

def simulated_annealing():
    current_solution = random.uniform(-10, 10)
    current_cost = objective_function(current_solution)

    temperature = 1000
    cooling_rate = 0.95
    min_temperature = 0.001
    max_iterations = 1000

    best_solution = current_solution
    best_cost = current_cost

    while temperature > min_temperature:
        for _ in range(max_iterations):
            neighbor = current_solution + random.uniform(-1, 1)
            neighbor_cost = objective_function(neighbor)

            delta = neighbor_cost - current_cost

            if delta < 0 or random.random() < math.exp(-delta / temperature):
                current_solution = neighbor
                current_cost = neighbor_cost

                if current_cost < best_cost:
                    best_solution = current_solution
                    best_cost = current_cost

        temperature *= cooling_rate

    return best_solution, best_cost

solution, cost = simulated_annealing()
print("Best Solution:", solution)
print("Best Cost:", cost)