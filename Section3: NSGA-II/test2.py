import numpy as np
import random

def non_dominated_sorting(fitness_values):
    # Non-dominated sorting based on the objectives
    fronts = []
    dominated_by = [[] for _ in range(len(fitness_values))]
    dominates = [0] * len(fitness_values)
    rank = [0] * len(fitness_values)

    for i in range(len(fitness_values)):
        for j in range(i + 1, len(fitness_values)):
            if all(x <= y for x, y in zip(fitness_values[i], fitness_values[j])):
                dominates[i] += 1
                dominated_by[j].append(i)
            elif all(x <= y for x, y in zip(fitness_values[j], fitness_values[i])):
                dominates[j] += 1
                dominated_by[i].append(j)

    current_front = []
    for i in range(len(fitness_values)):
        if dominates[i] == 0:
            rank[i] = 1
            current_front.append(i)

    fronts.append(current_front)

    i = 0
    while current_front:
        next_front = []
        for ind in current_front:
            for neighbor in dominated_by[ind]:
                dominates[neighbor] -= 1
                if dominates[neighbor] == 0:
                    rank[neighbor] = i + 2
                    next_front.append(neighbor)

        i += 1
        current_front = next_front
        if current_front:
            fronts.append(current_front)

    return fronts

def calculate_crowding_distance(front, fitness_values):
    # Crowding distance calculation for individuals in a front
    num_objectives = len(fitness_values[0])
    distances = [0] * len(front)

    for obj_index in range(num_objectives):
        sorted_front = sorted(front, key=lambda x: fitness_values[x][obj_index])
        min_val = fitness_values[sorted_front[0]][obj_index]
        max_val = fitness_values[sorted_front[-1]][obj_index]

        if max_val == min_val:
            continue

        distances[sorted_front[0]] = distances[sorted_front[-1]] = float('inf')
        for i in range(1, len(front) - 1):
            distances[sorted_front[i]] += (fitness_values[sorted_front[i + 1]][obj_index] - fitness_values[sorted_front[i - 1]][obj_index]) / (max_val - min_val)

    return distances

def tournament_selection(population, fitness_values, tournament_size):
    # Tournament selection to choose parents for crossover
    selected_parents = []

    for _ in range(len(population)):
        tournament = random.sample(range(len(population)), min(tournament_size, len(population)))
        tournament_fitness = [fitness_values[ind] for ind in tournament]
        
        # Check if the tournament is empty (can happen if tournament_size > len(population))
        if not tournament_fitness:
            winner_index = random.choice(range(len(population)))
        else:
            winner_index = tournament[np.argmax([sum(fitness) for fitness in tournament_fitness])]
        
        selected_parents.append(winner_index)

    return selected_parents

def crossover(parent_one, parent_two):
    # Order-based crossover
    crossover_point = random.randint(1, len(parent_one) - 1)
    child_one = [-1] * len(parent_one)
    child_two = [-1] * len(parent_two)

    child_one[crossover_point:] = [gene for gene in parent_two if gene not in parent_one[:crossover_point]]
    child_two[crossover_point:] = [gene for gene in parent_one if gene not in parent_two[:crossover_point]]

    for i in range(crossover_point):
        if parent_one[i] not in child_one:
            child_one[i] = parent_one[i]
        if parent_two[i] not in child_two:
            child_two[i] = parent_two[i]

    return child_one, child_two

def mutate(individual):
    # Swap mutation
    mutation_point1 = random.randint(0, len(individual) - 1)
    mutation_point2 = random.randint(0, len(individual) - 1)

    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]

    return individual

def NSGA_II(graph):
    population_size = 50
    generations = 100
    num_vertices = len(graph)
    
    # Initialize population with random permutations of vertices
    population = [random.sample(range(num_vertices), num_vertices) for _ in range(population_size)]
    
    for generation in range(generations):
        # Evaluate population based on the communication time and number of vertices reached
        fitness_values = [(sum(graph[individual[i]][individual[i + 1]] for i in range(len(individual) - 1)), len(set(individual))) for individual in population]
        
        # Perform non-dominated sorting to identify the Pareto fronts
        pareto_fronts = non_dominated_sorting(fitness_values)
        
        # Assign crowding distance to individuals to maintain diversity
        crowding_distances = [calculate_crowding_distance(front, fitness_values) for front in pareto_fronts]
        
        # Select parents for crossover using tournament selection
        parents = tournament_selection(population, fitness_values, tournament_size=2)
        
        # Generate new offspring through crossover and mutation
        offspring_population = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = population[parents[i]], population[parents[i + 1]]
            child1, child2 = crossover(parent1, parent2)
            offspring_population.extend([mutate(child1), mutate(child2)])
        
        # Create the new population by combining parents and offspring
        population = parents + offspring_population
    
    # Evaluate final population
    final_fitness_values = [(sum(graph[individual[i]][individual[i + 1]] for i in range(len(individual) - 1)), len(set(individual))) for individual in population]
    final_pareto_fronts = non_dominated_sorting(final_fitness_values)
    
    # Select the best individual from the final Pareto front as the solution
    best_individual = min(final_pareto_fronts[0], key=lambda x: final_fitness_values[x][0])
    
    # Extract the path, time and number of vertices from the best individual
    best_path = population[best_individual]
    time = sum(graph[best_path[i]][best_path[i + 1]] for i in range(len(best_path) - 1))
    vertices = len(set(best_path))
    
    return best_path, time, vertices

# Example usage:
graph = np.array([[0, 2, 3], [2, 0, 1], [3, 1, 0]])
best_path, time, vertices = NSGA_II(graph)
print("Minimum best path:", best_path)
print("With time:", time)
print("And number of vertices:", vertices)
