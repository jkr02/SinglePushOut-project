import igraph as ig
import Productions.production as production

class P8(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # [a-z,A-Z] -> [a-z,A-Z] -- zmiana labela wierzchołka
        if len(array) == 2 and array[0] < g.vcount():
            g.vs[array[0]]['Etykieta'] = array[1]
    @staticmethod
    def to_string():
        return "Production 8"
    @staticmethod
    def specification():
        return "L: [a-z,A-Z]\nR: [a-z,A-Z]"