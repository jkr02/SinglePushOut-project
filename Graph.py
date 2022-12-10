import pandas as pd
import igraph

def make_graph():
    labels = pd.read_excel('Input.xlsx', sheet_name='Labels')
    edges = pd.read_excel('Input.xlsx', sheet_name='Graph')
    g = igraph.Graph()
    for i in range(len(labels['no'].values)):
        name = labels['no'].values[i]
        g.add_vertex(name)
        g.vs[i]["label"]=labels['labels'].values[i]
    for i in range(len(edges.values)):
        for j in range(len(edges.values[i])):
            if edges.values[i][j]>0:
                g.add_edge(i, j)
                g.es[g.get_eid(i,j)]['weight']=edges.values[i][j]
def get_vertex(graph, name):
    return graph.vs[list(graph.vs['name']).index(name)]
make_graph()
