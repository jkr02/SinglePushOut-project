import igraph as ig
import Productions.production as production

# Nie dodałem etykiet krawędzi, jak ustalimy jak chcemy to robić to dodam (tworzy puste krawędzie)

class P6(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # (A1 -> A2) -> (C <- A1 -> A2' -> B)
        if len(array) == 2 and max(array) < g.vcount() and g.are_connected(array[0], array[1])\
                and str(g.vs[array[0]]['Etykieta'])=='A' and str(g.vs[array[1]]['Etykieta'])=='A':
            g.add_vertices(2)
            g.vs[g.vcount()-2:]['Etykieta']=['C', 'B']   
            g.vs[array[1]]['Etykieta']="A'"
            g.add_edges([(array[0], g.vcount()-2), (array[1],g.vcount()-1)])
            g.es[g.vcount() - 2:]['Etykieta'] = ['b', 'a']
            
    @staticmethod
    def to_string():
        return "Production 6"
    @staticmethod
    def specification():
        return "L: A1 -> A2\nR: C <- A1 -> A2' -> B"

# a = ig.Graph([(0,1)])
# a.vs['Etykieta']=['A','A']
# print(len(a.vs))
# p6 = P6()
# p6.produce(a, [0,1])
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