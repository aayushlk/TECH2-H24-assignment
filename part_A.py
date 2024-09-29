"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import math
import numpy as np

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    su=0
    sqauresu=0
    count=0
    for i in x:
        su+=i
        sqauresu+=i**2
        count+=1
    
    mean=su/count
    squaremean=sqauresu/count
    var=squaremean-mean**2
    sd=math.sqrt(var)
    return sd
    

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    mean=sum(x)/len(x)
    squarelst=[]
    for i in x:
        squarelst.append(i**2)
    
    squaremean=sum(squarelst)/len(x)
    
    var=squaremean-mean**2
    sd=math.sqrt(var)
    return sd

num_lst=[1,2,3,4,5]
loops=std_loops(num_lst)
func=std_builtin(num_lst)
real=np.std(num_lst)

print(loops,func,real)
