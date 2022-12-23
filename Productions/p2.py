import igraph as ig
import Productions.production

class P2(Productions.production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # A-a->(B1 B) -> A-a>(B2 B-b>C)
        if len(array)==3 \
                and g.vs[array[0],array[1],array[2]]['Etykieta']==['A', 'B', 'B']\
                and g.vs[g.get_eids([(array[0], array[1]), (array[0], array[2])])]['Etykieta']==['a', 'a']:
            g.add_vertices(2)
            g.vs[g.vcount()-2:]['Etykieta']=['B', 'C']
            g.add_edges([(array[0], g.vcount()-2), (array[2], g.vcount()-1)])
            g.es[g.vcount() - 2:]['Etykieta'] = ['a', 'b']
            g.delete_vertices(array[1])
    @staticmethod
    def specification():
        return "L: A-a->(B1 B)\nP: A-a->(B2 B-b->C)"
    @staticmethod
    def to_string():
        return "Production 2"
# a = ig.Graph([(0,1), (0,2), (2,3)])
# a.vs['Etykieta']=['A', 'B', 'B', 'C']
# a.es['Etykieta']=['a', 'a', 'b']
# print(len(a.vs))
# # print(a.es[a.get_eids([(0,1),(2,3)])]['Etykieta'])
# p2 = P2()
# p2.produce(a, [0,1,2])
# print(len(a.vs))
# print(a.get_edgelist())
# print(a.vs['Etykieta'])