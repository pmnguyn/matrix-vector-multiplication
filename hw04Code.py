import numpy as np

def innerProduct(a,b):
    """
    Takes two vectors a and b, of equal length, and returns their inner product
    """
    res = 0
    for i in range(len(a)):
        res += a[i]*b[i]
    return res

def AxIP(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    m, n = np.shape(A)
    res = np.array([])
    for i in range(len(A)):
        res = np.append(res, innerProduct(A[i,:].T, x))
    return res

def AxVS(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    m, n = np.shape(A)
    res = np.array([])
    for i in range(len(A)):
        res = np.append(res, 0)
    for i in range(len(A[0])):
        res += (A[:,i]*x[i])
    return res
