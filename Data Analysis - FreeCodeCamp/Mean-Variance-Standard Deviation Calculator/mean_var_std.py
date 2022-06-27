from matplotlib.cbook import flatten
import numpy as np


def calculate(list):
    # Transforma a lista em uma matrix 3x3
    matrix = np.array(list).reshape(3, 3)
    axis1 = matrix(axis=0)
    axis2 = matrix(axis=1)
    flattened = matrix
    
    
    calculations = {
        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened]
    }
    axis1 = matrix.mean(axis=0)
    calculations['mean'][0] = matrix.mean(axis=0)
    return calculations
