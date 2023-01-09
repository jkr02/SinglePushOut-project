import igraph as ig
import Productions.production as production

class P7(production.Production):
    @staticmethod
    def produce(g: ig.Graph, array: list): # (A B) -> (A -> B) -- dowolne dwa wierzchołki są łączone 
        if len(array) == 2 and max(array) < g.vcount() and not g.are_connected(array[0], array[1]):
            g.add_edges([(array[0], array[1])])
            
    @staticmethod
    def to_string():
        return "Production 7"
    @staticmethod
    def specification():
        return "L: A B\nR: A -> B"