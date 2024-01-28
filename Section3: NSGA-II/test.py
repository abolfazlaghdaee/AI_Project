import numpy as np
import random
import math

# Example Weighted Adjacency Matrix (4 vertices)
weighted_graph = np.array([
    [0, 2, 3, 0],
    [2, 0, 0, 5],
    [3, 0, 0, 4],
    [0, 5, 4, 0]
])

# Number of vertices in the graph
num_vertices = len(weighted_graph)

# Function to calculate the total time in the graph
def calculate_total_time(graph, path):
    total_time = 0
    for i in range(len(path) - 1):
        total_time += graph[path[i]][path[i + 1]]
    return total_time

# Function to find index of list
def index_of(a, lst):
    for i in range(len(lst)):
        if lst[i] == a:
            return i
    return -1

# Function to sort by values
def sort_by_values(lst, values):
    sorted_list = []
    while len(sorted_list) != len(lst):
        if index_of(min(values), values) in lst:
            sorted_list.append(index_of(min(values), values))
        values[index_of(min(values), values)] = math.inf
    return sorted_list

# Function to carry out NSGA-II's fast non-dominated sort
def fast_non_dominated_sort(values1, values2):
    S = [[] for _ in range(len(values1))]
    front = [[]]
    n = [0 for _ in range(len(values1))]
    rank = [0 for _ in range(len(values1))]

    for p in range(len(values1)):
        S[p] = []
        n[p] = 0
        for q in range(len(values1)):
            if (values1[p] > values1[q] and values2[p] > values2[q]) or \
               (values1[p] >= values1[q] and values2[p] > values2[q]) or \
               (values1[p] > values1[q] and values2[p] >= values2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (values1[q] > values1[p] and values2[q] > values2[p]) or \
                 (values1[q] >= values1[p] and values2[q] > values2[p]) or \
                 (values1[q] > values1[p] and values2[q] >= values2[p]):
                n[p] += 1
        if n[p] == 0:
            rank[p] = 0
            if p not in front[0]:
                front[0].append(p)

    i = 0
    while front[i]:
        Q = []
        for p in front[i]:
            for q in S[p]:
                n[q] -= 1
                if n[q] == 0:
                    rank[q] = i + 1
                    if q not in Q:
                        Q.append(q)
        i += 1
        front.append(Q)

    del front[-1]
    return front

# Function to calculate crowding distance
def crowding_distance(values1, values2, front):
    distance = [0] * len(front)
    sorted1 = sort_by_values(front, values1[:])
    sorted2 = sort_by_values(front, values2[:])
    distance[0] = distance[len(front) - 1] = float('inf')
    for k in range(1, len(front) - 1):
        if max(values2) - min(values2) != 0:
            distance[k] += (values1[sorted1[k + 1]] - values1[sorted1[k - 1]]) / (max(values1) - min(values1))
            distance[k] += (values2[sorted2[k + 1]] - values2[sorted2[k - 1]]) / (max(values2) - min(values2))
    return distance

# Function to carry out the crossover
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

# Main program starts here
pop_size = 20
max_gen = 100

# Initialization
min_x = 0
max_x = num_vertices  # Set the number of vertices according to your graph
solution = [list(np.random.permutation(range(max_x))) for _ in range(pop_size)]  # Use max_x instead of num_vertices
gen_no = 0

while gen_no < max_gen:
    function1_values = [calculate_total_time(weighted_graph, solution[i]) for i in range(pop_size)]
    function2_values = [len(set(solution[i])) for i in range(pop_size)]

    non_dominated_sorted_solution = fast_non_dominated_sort(function1_values[:], function2_values[:])
    print("The best front for Generation number ", gen_no, " is")
    for valuez in non_dominated_sorted_solution[0]:
        print(solution[valuez], end=" ")
    print("\n")

    crowding_distance_values = []
    for i in range(len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:], function2_values[:],
                                                          non_dominated_sorted_solution[i][:]))

    solution2 = solution[:]

    # Generating offsprings
    while len(solution2) != 2 * pop_size:
        a1 = random.randint(0, pop_size - 1)
        b1 = random.randint(0, pop_size - 1)
        solution2.append(crossover(solution[a1], solution[b1]))

    function1_values2 = [calculate_total_time(weighted_graph, solution2[i]) for i in range(2 * pop_size)]
    function2_values2 = [len(set(solution2[i])) for i in range(2 * pop_size)]

    non_dominated_sorted_solution2 = fast_non_dominated_sort(function1_values2[:], function2_values2[:])
    crowding_distance_values2 = []
    for i in range(len(non_dominated_sorted_solution2)):
        crowding_distance_values2.append(crowding_distance(function1_values2[:], function2_values2[:],
                                                           non_dominated_sorted_solution2[i][:]))

    new_solution = []
    for i in range(len(non_dominated_sorted_solution2)):
        non_dominated_sorted_solution2_1 = [
            index_of(non_dominated_sorted_solution2[i][j], non_dominated_sorted_solution2[i]) for j in
            range(len(non_dominated_sorted_solution2[i]))]
        front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_values2[i][:])
        front = [non_dominated_sorted_solution2[i][front22[j]] for j in range(len(non_dominated_sorted_solution2[i]))]
        front.reverse()
        for value in front:
            new_solution.append(value)
            if len(new_solution) == pop_size:
                break
        if len(new_solution) == pop_size:
            break

    solution = [solution2[i] for i in new_solution]
    gen_no += 1

# Extract the Pareto front and display the results
best_solution_index = non_dominated_sorted_solution[0][0]
best_path = solution[best_solution_index]
best_time = function1_values[best_solution_index]
num_reached_vertices = function2_values[best_solution_index]

print("\nBest Path:", best_path)
print("Total Time:", best_time)
print("Number of Vertices Reached:", num_reached_vertices)
