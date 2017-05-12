# -*- coding: utf-8 -*-
"""
Created on Fri May 12 16:03:04 2017

@author: ijmadrid
"""

import numpy as np
import Q1 as q1
import clustering_spectral as clusp

def main(n,k,cin,cout,option):
    pin = cin/n
    pout = cout/n
    
    B = np.ones((k,k))*pout
    
    for i in range(k):
        B[i,i] = pin
    
    print B
    
    V = np.arange(n)
    C0 = np.ones(n)
    C0[:n/2] = 0
    
    print C0
    # Stochastic block model
    A = q1.stochastic_block_model(V,C0,B)
    
    # Clustering
    C1 = clusp.clustering_spectral(A,k,option)

cin = 90.
cout = 20.

main(100,2,cin,cout,1)