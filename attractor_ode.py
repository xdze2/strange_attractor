from numba import jit, float64
import numpy as np

@jit(float64[:](float64[:], float64), nopython=True)
def thomas_attractor(xyz, b):
    ''' ODE for Thomas attractor
        xyz: point position, 1d array, float64
        b: coefficient, float64
        
        use numba JIT
    '''
    sin_xyz = np.sin(xyz)
    dYdt = -b*xyz
    dYdt[0] += sin_xyz[1]
    dYdt[1] += sin_xyz[2]
    dYdt[2] += sin_xyz[0]
    return dYdt