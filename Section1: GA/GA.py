# Artificiall Intelligence Project Section1
# Under Supervision of Dr. Soheil-Shamaee 
# By: Abolfazl Aghdaee 9811152202
# The first Section is solving the problem by using Genetic Algorithm:

import random
import numpy as np  
from functions import Fitness, Crossover, Mutate, First_POP #Imported from functions.py file 


graph = np.array([[0, 3, 1, 0, 0],
                  [3, 0, 3, 0, 0], 
                  [1, 3, 0, 4, 0],
                  [0, 0, 4, 0, 5],
                  [0, 0, 0, 5, 0]])



def genetic_algorithm(graph,POP_size=50, generation= 500):
    num_vertex = graph.shape[0]


    POP=First_POP(POP_size, num_vertex)



    for generate in range(generation):
        fitness_num =[]


        for coromom in POP :
            fitness_score =Fitness(coromom, graph)
            fitness_num.append(fitness_score)




        select_POP= []


        for i in range(POP_size):
            tournament_size = 5
            tournament = random.sample(list(enumerate(fitness_num)), tournament_size)
            selected_index = max(tournament, key=lambda x: x[1])[0]
            select_POP .append(POP [selected_index])




        new_POP = []


        for i in range(0, POP_size, 2):

            parent1,parent2=select_POP [i], select_POP [i+1]
            
            child1, child2 = Crossover(parent1, parent2)
            new_POP.extend([child1, child2])

       
        for i in range(POP_size):
            new_POP[i] = Mutate(new_POP[i])

        POP  = new_POP

    fitness_num = []


    for coromom in POP:
        fitness_score = Fitness(coromom, graph)
        fitness_num.append(fitness_score)  


    best_coromom= POP[np.argmax([score[1] for score in fitness_num])]

    time, vertices= max(fitness_num, key=lambda x: x[1])




    return best_coromom,time, vertices







if __name__ == "__main__":


   
    best_path, time, vertices = genetic_algorithm(graph)
    # print("Best Path for Burning my graph", best_path)
    # print("Time", time)
    # print("Vertex", vertices)