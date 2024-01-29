import math

def index_of(a, lst):

    for i in range(len(lst)):
        if lst[i] == a:
            return i
    return -1

def sort_by_values(lst, values):
    sorted_list = []
    while len(sorted_list) != len(lst):
        if index_of(min(values), values) in lst:
            sorted_list.append(index_of(min(values), values))
        values[index_of(min(values), values)] = math.inf
    return sorted_list



def crowding_distance(value1, value2,front):


    distance = [0] * len(front)

    sorted1 =sort_by_values(front, value1[:])
    sorted2 =sort_by_values(front, value2[:])


    distance[0] = distance[len(front) - 1] =float('inf')


    for k in range(1, len(front) - 1):
        if max(value2) - min(value2) != 0:
            
            distance[k] += (value1[sorted1[k + 1]] - value1[sorted1[k - 1]]) / (max(value1) - min(value1))
            distance[k] += (value2[sorted2[k + 1]] - value2[sorted2[k - 1]]) / (max(value2) - min(value2))
    return distance