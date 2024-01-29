
import random

def crossover(parent_one, parent_two):
    point_of_crossover = random.randint(1, len(parent_one) - 1)
    child_one = parent_one[:point_of_crossover] + [gen for gen in parent_two if gen not in parent_one[:point_of_crossover]]
    child_two = parent_two[:point_of_crossover] + [gen for gen in parent_one if gen not in parent_two[:point_of_crossover]]

    # Perform mutation on child_one and child_two if needed
    child_one = mutation(child_one)
    child_two = mutation(child_two)

    return child_one, child_two

# Function to carry out the mutation operator
def mutation(solution):
    mutation_prob = random.random()
    if mutation_prob < 1:
        # Ensure uniqueness of vertices in the path
        unique_solution = list(set(solution))
        while len(unique_solution) < len(solution):
            unique_solution.append(random.choice([vertex for vertex in range(num_vertices) if vertex not in unique_solution]))
        return unique_solution
    return solution