import igraph as ig
import Productions.production as production

class P3(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # B -> (A -> B -> C)
        if len(array)==1 and str(g.vs[array[0]]['Etykieta'])=='B':
            g.add_vertices(2)
            g.vs[g.vcount()-2:]['Etykieta']=['A', 'C']
            g.add_edges([(array[0], g.vcount()-1), (g.vcount()-2, array[0])])
            g.es[g.vcount() - 2:]['Etykieta'] = ['a', 'b']
    @staticmethod
    def to_string():
        return "Production 3"
    @staticmethod
    def specification():
        return "L: B\nR: A -> B -> C"

# a = ig.Graph()
# a.add_vertices(1)
# a.vs['Etykieta']=['B']
# print(len(a.vs))
# p3 = P3()
# p3.produce(a, [0])
# print(len(a.vs))
# print(a.get_edgelist())
# print(list(a.vs()))
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(5,5))
# ig.plot(
#     a,
#     target=ax,
#     layout="circle", # print nodes in a circular layout
#     vertex_size=0.1,
#     vertex_color="steelblue",
#     vertex_frame_width=4.0,
#     vertex_frame_color="white",
#     vertex_label=a.vs["Etykieta"],
#     vertex_label_size=7.0,
#     edge_width=2,
#     edge_color="#7142cf")
# plt.show()