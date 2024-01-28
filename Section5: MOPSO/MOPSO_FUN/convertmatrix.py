import numpy as np
def convert_matrix(graph):
    """
    this function convert the matrix to new matrix that all zeros in last matrix 
    except zeros on diagonal chaned to infinity for calculating the correct time.
    """
    graph = graph.astype(float)

    diagonal= np.diag_indices(min(graph.shape))

    graph[graph == 0] =np.inf
    graph[diagonal] =0

    return graph