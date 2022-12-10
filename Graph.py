import pandas as pd
import igraph


# class Vertex:
#     def __init__(self, no, label):
#         self.no = no
#         self.label = label


def make_graph():
    labels = pd.read_excel('Input.xlsx', sheet_name='Labels')
    edges = pd.read_excel('Input.xlsx', sheet_name='Graph')
    g = igraph.Graph()
    for i in range(len(labels)):
        g.add_vertex(i)
        g.vs[i]["label"]=labels['Labels'][i]
    for i in range(len(edges.values)):
        for j in range(len(edges.values[i])):
            if edges.values[i][j]>0:
                g.add_edge(i, j)
                g.es[g.get_eid(i,j)]['weight']=edges.values[i][j]
    return g
make_graph()
