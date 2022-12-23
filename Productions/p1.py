import igraph as ig
from Productions import production

class P1(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # A -> (A -d-> B)
        if len(array)==1 and str(g.vs[array[0]]['Etykieta'])=='A':
            g.add_vertices(1)
            g.vs[len(g.vs)-1]['Etykieta']='B'
            g.add_edge(array[0], len(g.vs)-1)
            g.es[len(g.es)-1]['Etykieta']='d'
    @staticmethod
    def to_string():
        return "Production 1"
    @staticmethod
    def specification():
        return "L: A\nR: A-d->B"
# a = ig.Graph([(0,1), (0,2), (2,3)])
# a.vs['label']=['A', 'B', 'A', 'C']
# print(len(a.vs))
# p1 = P1()
# p1.produce(a, [0])
# print(len(a.vs))
# print(a.get_edgelist())
# print(list(a.vs()))
# fig, ax = plt.subplots(figsize=(5,5))
# ig.plot(
#     a,
#     target=ax,
#     layout="circle", # print nodes in a circular layout
#     vertex_size=0.1,
#     vertex_color="steelblue",
#     vertex_frame_width=4.0,
#     vertex_frame_color="white",
#     vertex_label=a.vs["label"],
#     vertex_label_size=7.0,
#     edge_width=2,
#     edge_color="#7142cf")
#
# plt.show()