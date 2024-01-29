
def calc_time(graph, path):
    time = 0


    for i in range(len(path) - 1):
        time += graph[path[i]][path[i + 1]]


    return time