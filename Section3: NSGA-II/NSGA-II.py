# Artificiall Intelligence Project Section3
# Under Supervision of Dr. Soheil-Shamaee 
# By: Abolfazl Aghdaee 9811152202
# The last Section is solving the problem by using NSGA-II Algorithm



import numpy as np
import random

from nsga_functions.time import calc_time
from nsga_functions.sort import sort_by_values , index_of, crowding_distance
from nsga_functions.non_dominate import non_dominated_sort
from nsga_functions.crossover_mutation import crossover, mutation


graph =  np.array([[0, 3, 1, 0, 0],
                  [3, 0, 3, 0, 0], 
                  [1, 3, 0, 4, 0],
                  [0, 0, 4, 0, 5],
                  [0, 0, 0, 5, 0]])



num_vertices = len(graph)
max_x = num_vertices 
pop_size = 20
max_gen = 10
    




min_x = 0
 
solution = []
for _ in range(pop_size):
    per = np.random.permutation(range(max_x))
    
    solution.append(list(per))
    
gen_no = 0

while gen_no < max_gen:

    function1_values = []
    for i in range(pop_size):
        function1_values.append(calc_time(graph, solution[i]))

    # also I wrote the fucntion2_vlaue by using ninja programming :))
    function2_values = [len(set(solution[i])) for i in range(pop_size)]



    non_dominated_sorted_solution = non_dominated_sort(function1_values[:], function2_values[:])


    print("The best front for Generation number ", gen_no, " is")
    for valuez in non_dominated_sorted_solution[0]:
        print(solution[valuez], end=" ")
        
    print("\n")

    crowding_distance_values = []
    for i in range(len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:], function2_values[:],non_dominated_sorted_solution[i][:]))

    solution2 = solution[:]

    while len(solution2) != 2* pop_size:

        a1 = random.randint(0, pop_size -1)
        b1 = random.randint(0, pop_size -1)


        child_one, child_two = crossover(solution[a1], solution[b1])

        solution2.extend([child_one, child_two])



    function1_value2 = []
    for i in range(2 * pop_size):
        time = calc_time(graph, solution2[i])
        function1_value2.append(time)



    function2_value2 = []
    for i in range(2 * pop_size):
        unique_elements = len(set(solution2[i]))
        function2_value2.append(unique_elements)


    non_dominated_sorted_solution2 = non_dominated_sort(function1_value2[:], function2_value2[:])



    crowding_distance_value2 = []
    for i in range(len(non_dominated_sorted_solution2)):
        crowding_distance_value2.append(crowding_distance(function1_value2[:], function2_value2[:],non_dominated_sorted_solution2[i][:]))




    new_solution = []
    for i in range(len(non_dominated_sorted_solution2)):



        non_dominated_sorted_solution2_1 = []
        for j in range(len(non_dominated_sorted_solution2[i])):
            index = index_of(non_dominated_sorted_solution2[i][j], non_dominated_sorted_solution2[i])
            
            non_dominated_sorted_solution2_1.append(index)
        front22 = sort_by_values(non_dominated_sorted_solution2_1[:], crowding_distance_value2[i][:])


        front = []
        for j in range(len(non_dominated_sorted_solution2[i])):

            front_element = non_dominated_sorted_solution2[i][front22[j]]
            
            front.append(front_element)
            

        front.reverse()


        for value in front:
            new_solution.append(value)
            if len(new_solution) == pop_size:
                break


        if len(new_solution) == pop_size:
            break

    solution = []
    for i in new_solution:
        solution2_i = solution2[i]
        
        solution.append(solution2_i) 
        
    gen_no += 1





if __name__ == '__main__':

    

    best_solution_index = non_dominated_sorted_solution[0][0]
    best_path = solution[best_solution_index]
    best_time = function1_values[best_solution_index]
    num_reached_vertices = function2_values[best_solution_index]

    # print("\nBest Path:", best_path)
    # print("Total Time:", best_time)
    # print("Number of Vertices Reached:", num_reached_vertices)
