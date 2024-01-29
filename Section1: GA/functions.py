import numpy as np 
import random



def First_POP(POP_size, num_vertex):
    POP = []


    for _ in range(POP_size):

        coromom = list(range(num_vertex))
        random.shuffle(coromom)
        POP.append(coromom)



    return POP




def Fitness(cormome, graph):
    TIME = 0
    
    vertex_covered = set()

    
    for i in range(len(cormome)- 1):
        root, target = cormome[i], cormome[i+1]


        if graph[root][target]!= 0:

            TIME += graph[root][target]
            vertex_covered.add(target)



    return TIME, len(vertex_covered)


def Crossover(parent_one, parent_two):


    point_of_crossover = random.randint(1,len(parent_one)-1)

    child_one = parent_one[:point_of_crossover] +[gen for gen in parent_two if gen not in parent_one[:point_of_crossover]]
    child_two = parent_two[:point_of_crossover] +[gen for gen in parent_one if gen not in parent_two[:point_of_crossover]]


    return child_one,child_two


def Mutate(coromom):
    """
    Note that this function is used for mutation 4 points 
    but instead we can apply this function for 2 points
    but I ran this function for 2 points and the result was not perfect, but whne i used for 4 point I got better results.  
    
    """


    mutation_point1= random.randint(0,len(coromom)- 1)
    mutation_point2= random.randint(0,len(coromom)- 1)

    mutation_point3=random.randint(0,len(coromom)- 1)
    mutation_point4=random.randint(0,len(coromom)- 1)

    coromom[mutation_point1],coromom[mutation_point2]= coromom[mutation_point2], coromom[mutation_point1]
    coromom[mutation_point3],coromom[mutation_point4]= coromom[mutation_point4], coromom[mutation_point3] 


    return coromom