
import numpy as np

def update_paths(paths, vel):


    new_paths = np.zeros_like(paths)


    for i in range(len(paths)):
        
        order = np.argsort(vel[i])
        new_paths[i] = paths[i][order]

        
    return new_paths
