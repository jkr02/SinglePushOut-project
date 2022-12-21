import igraph as ig
import production
class P1(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # A -> (A -> B)
        if len(array)==1 and str(g.vs[array[0]]['label'])=='A':
            g.add_vertices(1)
            g.vs[len(g.vs)-1]['label']='B'
            g.add_edge(array[0], len(g.vs)-1)
    @staticmethod
    def to_string():
        return "Production 1"
    @staticmethod
    def specification():
        return "L: A\nR: A->B"