import igraph as ig
import Productions.production as production

# Produkcja zmienia etykietę wierzchołka z małej na dużą literę

class P4(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # [a-z] -> [A-Z]
        if len(array)==1 and g.vs[array[0]]['Etykieta'].islower():
            g.vs[array[0]]['Etykieta']=g.vs[array[0]]['Etykieta'].upper()
    @staticmethod
    def to_string():
        return "Production 4"
    @staticmethod
    def specification():
        return "L: [a-z]\nR: [A-Z]"

# a = ig.Graph()
# a.add_vertices(2)
# a.vs['Etykieta']=['b', 'z']
# print(len(a.vs))
# p4 = P4()
# p4.produce(a, [0])
# p4.produce(a, [1])
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