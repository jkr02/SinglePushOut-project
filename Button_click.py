import igraph as ig
import matplotlib.pyplot as plt
from Excel_integration import excel
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
        if len(a) == 2 and not a[1].isdigit():
            try:
                self.array.append(int(a[0]))
                self.array.append(a[1])
            except:
                ""
        else:
            try:
                for i in a:
                    self.array.append(int(i))
            except:
                ""
    def vertexLabel(self):
        a = []
        for i in range(len(self.g.vs["Etykieta"])):
            a.append(self.g.vs[i]["Etykieta"] + " " +str(i))
        return a

    def pro1(self):
        p1.P1.produce(self.g,self.array)
        return self.vertexLabel()
    def pro2(self):
        Productions.p2.P2.produce(self.g, self.array)
        return self.vertexLabel()
    def pro3(self):
        Productions.p3.P3.produce(self.g, self.array)
        return self.vertexLabel()
    def pro4(self):
        Productions.p4.P4.produce(self.g, self.array)
        return self.vertexLabel()
    def pro5(self):
        Productions.p5.P5.produce(self.g, self.array)
        return self.vertexLabel()
    def pro6(self):
        Productions.p6.P6.produce(self.g, self.array)
        return self.vertexLabel()
    def pro7(self):
        Productions.p7.P7.produce(self.g, self.array)
        return self.vertexLabel()
    def pro8(self):
        Productions.p8.P8.produce(self.g, self.array)
        return self.vertexLabel()
    def pro9(self):
        Productions.p9.P9.produce(self.g, self.array)
        return self.vertexLabel()
    def pro10(self):
        Productions.p10.P10.produce(self.g, self.array)
        return self.vertexLabel()
    def pushGraph_to_excel(self,event):
        excel.push_to_excel(self.g)
