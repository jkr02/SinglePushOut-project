import igraph as ig
import Productions.production as production


class P9(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # (A -> B) -> (A B) -- dowolne dwa zostają rozdzielone
        if len(array) == 2 and max(array) < g.vcount() :
            if g.are_connected(array[0], array[1]):
                g.delete_edges([(array[0], array[1])])
            if g.are_connected(array[1], array[0]):
                g.delete_edges([(array[1], array[0])])
            
    @staticmethod
    def to_string():
        return "Production 9"
    @staticmethod
    def specification():
        return "L: A -> B\nR: A B"