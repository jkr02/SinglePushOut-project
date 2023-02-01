import igraph as ig
import Productions.production as production

class P5(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # (A -> B -> C) -> (A -> C) litery mogą być dowolne (zostaje usunięty wierzchołek w środku)
        if len(array) == 3 \
                and max(array) < g.vcount()\
                and g.are_connected(array[0], array[1])\
                and g.are_connected(array[1], array[2]):
                # and str(g.vs[array[0]]['Etykieta'])=='A'\
                # and str(g.vs[array[1]]['Etykieta'])=='B'\
                # and str(g.vs[array[2]]['Etykieta'])=='C'\
            if not g.are_connected(array[0], array[2]):
                g.add_edges([(array[0],array[2])])
                g.es[g.vcount() - 1]['Etykieta'] = 'b'
            g.delete_edges([(array[0], array[1]),(array[1], array[2])])
            g.delete_vertices(array[1])
    @staticmethod
    def to_string():
        return "Production 5"
    @staticmethod
    def specification():
        return "L: A -> B -> C\nR: A -> C"

# a = ig.Graph([(0,1),(1,2)])
# a.vs['Etykieta']=['D','B','C']
# print(len(a.vs))
# p5 = P5()
# p5.produce(a, [0,1,2])
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