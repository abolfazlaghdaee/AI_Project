import numpy as np

def calc_time(path, graph):
    time = 0

    
    for i in range(len(path)-1):

        start = path[i]
        finish = path[i+1]

        time = time +graph[start][finish] 
    return time
