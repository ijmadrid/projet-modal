# -*- coding: utf-8 -*-
"""
Created on Fri May  5 16:17:57 2017

@author: ijmadrid
"""

from igraph import *
import numpy as np


def stochastic_block_model(V,C,B):
    """
    Input :     V : Vecteur de noeuds, 
                C : Vecteur classes C, 
                B : Matrice de probas
                
    Ouput :     A : Matrice d'adjacence du graphe (V,E) generé par B
    """
    n = len(V)
    A = np.zeros((n,n))    
    for u in range(len(V)):
        for v in range(len(V)):
            if ( u <= v and np.random.rand() <= B[C[u],C[v]]):
                ##  On fait l'arête u<->v
                A[u][v] = A[v][u] = 1
    
    return A

def graph_from_A(A):
    """
    Input :     A : Matrice d'adjacence
    
    Output :    igraph.Graph object
    """
    nV = len(A)
    g = Graph()
    g.add_vertices(nV)
    g.vs["label"]=range(nV)
    
    for i in range(nV):
        for j in range(nV):
            if (A[i,j] == 1 and i <= j):
                g.add_edges([(i,j)])
    
    return g

def graph_plot(g,savefile_name):
    layout = g.layout("kk")
    plot(g, savefile_name+"_graph.pdf", layout = layout)
    
def test0():
    testA = np.array([[1,0,1,1],
                      [0,0,1,0],
                      [1,1,1,1],
                      [1,0,1,0]])
    
    graph_plot(graph_from_A(testA),"test0")



def test1():
    V = np.arange(10)
    C = [0,0,0,1,1,1,2,2,0,0]
    
    B = np.array([[0.8,0.9,0.0],
                 [0.9,0.5,0.9],
                 [0.0,0.9,0.7]])
    
    A = stochastic_block_model(V,C,B)
    graph = graph_from_A(A)
    
    colors = []
    for i in range(0, max(C)+1):
        colors.append('%06X' % np.random.randint(0, 0xFFFFFF))
    for vertex in graph.vs():
        vertex["color"] = str('#') + colors[C[vertex.index]]
    
    graph_plot(graph,"test1")

def visualisation():
    A = np.load("matrices/file1.npy")
    C = np.load("matrices/file2.npy")

    graph = graph_from_A(A)
    
    colors = []
    for i in range(0, max(C)+1):
        colors.append('%06X' % np.random.randint(0, 0xFFFFFF))
    for vertex in graph.vs():
        vertex["color"] = str('#') + colors[C[vertex.index]]
    
    graph_plot(graph,"option 1 Arnaud")