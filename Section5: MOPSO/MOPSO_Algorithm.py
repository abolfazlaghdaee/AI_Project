# Artificiall Intelligence Project Section5
# Under Supervision of Dr. Soheil-Shamaee 
# By: Abolfazl Aghdaee 9811152202
# The last Section is solving the problem by using MOPSO Algorithm:



import numpy as np

from  MOPSO_FUN.calc_time import calc_time
from MOPSO_FUN.convertmatrix import convert_matrix
from MOPSO_FUN.updata_path import update_paths


graph = np.array([
                  [0, 3, 1, 0, 0],
                  [3, 0, 3, 0, 0], 
                  [1, 3, 0, 4, 0],
                  [0, 0, 4, 0, 5],
                  [0, 0, 0, 5, 0]] )



graph = convert_matrix(graph)




def mopso_algorithm(graph, num_POP=30, iter=100, w=0.5, c1=1, c2=2):
    num_vertex = len(graph)
    
    POP = np.empty((num_POP, num_vertex), dtype=int)
    for i in range(num_POP):
        POP[i] = np.random.permutation(num_vertex)



    vel = np.zeros((num_POP, num_vertex),dtype=int)
    
    PBest = np.copy(POP)


    best_times = np.empty(len(POP))

    for i in range(len(POP)):
        best_times[i] = calc_time(POP[i], graph) 
    

    min_index = 0
    min_value = best_times[0]

    for i in range(1, len(best_times)):
        if best_times[i] < min_value:
            min_value = best_times[i]
            min_index = i

    globalbest_path = PBest[min_index]


    global_best_time = np.min(best_times)
    
    for i in range(iter): 

        R1 = np.random.uniform(0, 1,(num_POP, num_vertex))
        R2 = np.random.uniform(0, 1,(num_POP, num_vertex))

        vel = w* vel+ c1 *R1 *(PBest- POP) + c2* R2* (globalbest_path-POP)
        
        
        POP = update_paths(POP, vel)
        
        
        times = np.empty(len(POP))


        for i in range(len(POP)):
            times[i] = calc_time(POP[i], graph)
        
   
            
        improved_indices = np.where(times < best_times)
        PBest[improved_indices] = POP[improved_indices]


        best_times[improved_indices] = times[improved_indices]
        
       

        if np.min(times) < global_best_time:

            globalbest_path = POP[np.argmin(times)]
            global_best_time = np.min(times)
    

    return globalbest_path, global_best_time








if __name__ == "__main__":
        best_path, best_time =mopso_algorithm(graph)

        # print('Best Path:', best_path)
        # print('Best Time:', best_time)
        # print('Number of Vertices:',len(best_path))
