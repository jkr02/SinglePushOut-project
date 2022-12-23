import igraph as ig
import matplotlib.pyplot as plt

import Productions.p1 as p1
import Productions.p2 as p2
import Productions.production
from matplotlib.widgets import *
class BClick:
    def __init__(self, g: ig.Graph):
        self.g = g
        self.array=[]
    def assignVerticles_to_production(self, text: str):
        a=text.split(" ")
        self.array=[]
        try:
            for i in a:
                self.array.append(int(i))
        except:
            ""
    def drawGraph(self):
        a = []
        for i in range(len(self.g.vs["Etykieta"])):
            a.append(self.g.vs[i]["Etykieta"] + str(i))
        fig, ax = plt.subplots()
        ig.plot(self.g,
                target=ax,
                layout="circle",  # print nodes in a circular layout
                vertex_size=0.5,
                vertex_color="steelblue",
                vertex_frame_width=4.0,
                vertex_frame_color="white",
                vertex_label=a,
                edge_label=self.g.es["Etykieta"],
                vertex_label_size=10,
                edge_label_size=7.0,
                edge_width=2,
                edge_color="#7142cf"
                )
        plt.show()
    def pro1(self, event):
        p1.P1.produce(self.g,self.array)
        self.drawGraph()
        # a = []
        # for i in range(len(self.g.vs["Etykieta"])):
        #     a.append(self.g.vs[i]["Etykieta"] + str(i))
        # fig, ax = plt.subplots()
        # ig.plot(self.g,
        #         target=ax,
        #         layout="circle",  # print nodes in a circular layout
        #         vertex_size=0.5,
        #         vertex_color="steelblue",
        #         vertex_frame_width=4.0,
        #         vertex_frame_color="white",
        #         vertex_label=a,
        #         edge_label=self.g.es["Etykieta"],
        #         vertex_label_size=10,
        #         edge_label_size=7.0,
        #         edge_width=2,
        #         edge_color="#7142cf"
        #         )
        # plt.show()
    def pro2(self, event):
        Productions.p2.P2.produce(self.g, self.array)
        self.drawGraph()