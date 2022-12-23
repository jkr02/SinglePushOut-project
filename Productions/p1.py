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
# a = ig.Graph([(0,1), (0,2), (2,3)])
# a.vs['label']=['A', 'B', 'A', 'C']
# print(len(a.vs))
# p1 = P1()
# p1.produce(a, [0])
# print(len(a.vs))
# print(a.delete_vertices([0]))
# print(a.get_edgelist())