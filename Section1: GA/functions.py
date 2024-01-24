import numpy as np 
import random



def First_POP(POP_size, num_vertex):
    population = []


    for _ in range(POP_size):

        coromom = list(range(num_vertex))
        random.shuffle(coromom)
        population.append(coromom)



    return population




def calcFitness(individual, graph):
    total_time = 0
    vertices_covered = set()

    
    for i in range(len(individual)- 1):
        root, target = individual[i], individual[i+1]
        if graph[root][target] != 0:
            total_time += graph[root][target]
            vertices_covered.add(target)



    return total_time, len(vertices_covered)


def crossover(parent1, parent2):


    crossover_point = random.randint(1, len(parent1)-1)

    child1 = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [gene for gene in parent1 if gene not in parent2[:crossover_point]]


    return child1, child2


def mutate(coromom):


    mutation_point1 = random.randint(0, len(coromom)- 1)
    mutation_point2 = random.randint(0, len(coromom)- 1)

    coromom[mutation_point1], coromom[mutation_point2] = coromom[mutation_point2], coromom[mutation_point1]


    return coromom