import igraph as ig
import matplotlib.pyplot as plt

import Productions.p1 as p1
import Productions.p2 as p2
import Productions.p3 as p3
import Productions.p4 as p4
import Productions.p5 as p5
import Productions.p6 as p6
import Productions.p7 as p7
import Productions.p8 as p8
import Productions.p9 as p9
import Productions.p10 as p10
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
            a.append(self.g.vs[i]["Etykieta"] + " " +str(i))
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
    def pro2(self, event):
        Productions.p2.P2.produce(self.g, self.array)
        self.drawGraph()
    def pro3(self, event):
        Productions.p3.P3.produce(self.g, self.array)
        self.drawGraph()
    def pro4(self, event):
        Productions.p4.P4.produce(self.g, self.array)
        self.drawGraph()
    def pro5(self, event):
        Productions.p5.P5.produce(self.g, self.array)
        self.drawGraph()
    def pro6(self, event):
        Productions.p6.P6.produce(self.g, self.array)
        self.drawGraph()
    def pro7(self, event):
        Productions.p7.P7.produce(self.g, self.array)
        self.drawGraph()
    def pro8(self, event):
        Productions.p8.P8.produce(self.g, self.array)
        self.drawGraph()
    def pro9(self, event):
        Productions.p9.P9.produce(self.g, self.array)
        self.drawGraph()
    def pro10(self, event):
        Productions.p10.P10.produce(self.g, self.array)
        self.drawGraph()