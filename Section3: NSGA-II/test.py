import random
import numpy as np

def evaluate(individual, graph):
    time_taken = sum(graph[individual[i-1]][individual[i]] for i in range(len(individual)) if graph[individual[i-1]][individual[i]] != 0)
    num_vertices_covered = len(set(individual))
    return time_taken, -num_vertices_covered  # Negative for maximization  # Negative for maximization # Negative for maximization

def non_dominated_sort(population):
    fronts = [[]]
    S = [[] for _ in range(len(population))]
    n = [0 for _ in range(len(population))]
    rank = [0 for _ in range(len(population))]

    for p in range(len(population)):
        S[p] = []
        n[p] = 0
        for q in range(len(population)):
            if dominates(population[p], population[q]):
                S[p].append(q)
            elif dominates(population[q], population[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            fronts[0].append(p)

    i = 0
    while fronts[i]:
        Q = []
        for p in fronts[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    Q.append(q)
        i += 1
        fronts.append(Q)

    del fronts[-1]  # Remove empty front
    return fronts

def dominates(p, q):
    return all(pi <= qi for pi, qi in zip(p, q)) and any(pi < qi for pi, qi in zip(p, q))

def crowding_distance_sort(front, distances):
    sorted_front = sorted(front, key=lambda x: distances[x], reverse=True)
    return sorted_front

def crowding_distance(front, objectives):
    distances = [0.0] * len(front)
    num_objectives = len(objectives[0])  # Fix here

    if len(front) > 1:
        distances[front[0]] = distances[front[-1]] = float('inf')
        if len(front) > 2:
            for i in range(num_objectives):
                front = sorted(front[1:-1], key=lambda x: objectives[x][i])  # Exclude the endpoints

                if objectives[front[-1]][i] == objectives[front[0]][i]:
                    continue

                normalization_factor = objectives[front[-1]][i] - objectives[front[0]][i]
                for j in range(len(front)):
                    distances[front[j]] += (objectives[front[j+1]][i] - objectives[front[j-1]][i]) / normalization_factor

    return distances




def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [v for v in parent2 if v not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [v for v in parent1 if v not in parent2[:crossover_point]]
    return child1, child2

def mutate(individual):
    mutation_point1, mutation_point2 = random.sample(range(len(individual)), 2)
    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual

def genetic_algorithm(graph, population_size, generations):
    population = [random.sample(range(len(graph)), len(graph)) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate population
        objectives = [evaluate(individual, graph) for individual in population]
        objectives = list(map(list, zip(*objectives)))  # Transpose the objectives list


        # Non-dominated sorting
        fronts = non_dominated_sort(objectives)

        # Crowding distance assignment
        distances = [crowding_distance_sort(front, objectives) for front in fronts]
        distances = [crowding_distance(front, objectives) for front in fronts]

        # Select parents for crossover
        parents = []
        for front in fronts:
            parents.extend(crowding_distance_sort(front, distances)[:2])

        # Crossover and mutation
        new_population = []
        for i in range(0, len(parents), 2):
            parent1 = population[parents[i]]
            parent2 = population[parents[i+1]]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

    # Find the best individual on the last Pareto front
    last_front = fronts[-1]
    best_index = min(last_front, key=lambda x: objectives[x])
    best_individual = population[best_index]
    time_taken, num_vertices_covered = evaluate(best_individual, graph)

    return best_individual, time_taken, num_vertices_covered

# Example usage:
graph = np.array([[0, 3, 1, 0, 0],
                  [3, 0, 3, 0, 0], 
                  [1, 3, 0, 4, 0],
                  [0, 0, 4, 0, 5],
                  [0, 0, 0, 5, 0]])
print(graph)
population_size = 100
generations = 50
result = genetic_algorithm(graph, population_size, generations)
print("Best Path:", result[0])
print("Time Taken:", result[1])
print("Number of Vertices Covered:", -result[2])
