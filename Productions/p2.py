import igraph as ig
import production

class P2(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # A->(B1 B) -> A-> (B2 B->C)
        if len(array)==3 and str(g.vs[array[0]]['label'])=='A' and str(g.vs[array[1]]['label'])=='B' and str(g.vs[array[2]]['label'])=='B':
            g.delete_vertices(array[1])
            g.add_vertices(2)
            g.vs[g.vcount()-2:]['label']=['B', 'C']
            g.add_edges([(array[0], g.vcount()-2), (array[2], g.vcount()-1)])
    @staticmethod
    def specification():
        return "L: A->(B1 B)\nP: A->(B2 B->C)"
    @staticmethod
    def to_string():
        return "Production 2"
# a = ig.Graph([(0,1), (0,2), (2,3)])
# a.vs['label']=['A', 'B', 'B', 'C']
# print(len(a.vs))
# p2 = P2()
# p2.produce(a, [0,1,2])
# print(len(a.vs))
# print(a.get_edgelist())
# print(a.vs['label'])