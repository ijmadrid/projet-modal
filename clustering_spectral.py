# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:41:31 2017

@author: ijmadrid
"""

"""
Clustering spectral
"""

import numpy as np

def clustering_spectral(A, k, option):
    """
    Fait le clustering spectral sur le graph definit par la matrice d'adjacence A
    NB : A est symetrique (graph non orienté)
    
    Input :     np.array([[]])  A : matrice d'adjacence
                int             k : nombre de classes
                int        option : 1 ou 2 
    """
    if option == 1:
        
        eigvec, eigval = np.linalg.eigh(A)
        
        U = np.zeros((n,k))
        
        for i in range(n):
            U[:,i] = eigvec[:,-i-1]