# Artificiall Intelligence Project
# Under Supervsion of Dr. Shamaee 
# By: Abolfazl Aghdaee 9811152202
# The first Section: 



import numpy as np
import random
from functions import calcFitness, crossover, mutate, First_POP #Imported from functions.py file to calculate fitness


graph = np.array([[0, 3, 1, 0, 0],
                  [3, 0, 2, 0, 0], 
                  [1, 2, 0, 4, 0],
                  [0, 0, 4, 0, 5],
                  [0, 0, 0, 5, 0]])



def genetic_algorithm(graph,POP_size=50, generations= 1000):
    num_vertex = len(graph)
    population = First_POP(POP_size, num_vertex)



    for generation in range(generations):
        fitness_scores = []
        for coromom in population:
            fitness_score = calcFitness(coromom, graph)
            fitness_scores.append(fitness_score)




        selected_population = []

        for i in range(POP_size):
            tournament_size = 5
            tournament = random.sample(list(enumerate(fitness_scores)), tournament_size)
            selected_index = max(tournament, key=lambda x: x[1])[0]
            selected_population.append(population[selected_index])




        new_POP = []
        for i in range(0, POP_size, 2):

            parent1, parent2 = selected_population[i], selected_population[i+1]
            
            child1, child2 = crossover(parent1, parent2)
            new_POP.extend([child1, child2])

       
        for i in range(POP_size):
            new_POP[i] = mutate(new_POP[i])

        population = new_POP

    fitness_scores = []
    for coromom in population:
        fitness_score = calcFitness(coromom, graph)
        fitness_scores.append(fitness_score)  


    best_coromom = population[np.argmax([score[1] for score in fitness_scores])]

    time, vertices= max(fitness_scores, key=lambda x: x[1])




    return best_coromom, time, vertices







if __name__ == "__main__":


    print("My Graph is:","\n",graph)
    best_path, time, vertices = genetic_algorithm(graph)
    print("Best Path for Burning my graph", best_path)
    print("Time", time)
    print("Vertices", vertices)