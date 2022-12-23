import igraph as ig
class Production:
    @staticmethod
    def produce(g: ig.Graph, array: list):
        raise NotImplementedError

    @staticmethod
    def to_string():
        raise NotImplementedError
    @staticmethod
    def specification():
        return NotImplementedError