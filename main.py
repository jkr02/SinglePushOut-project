from Excel_integration import excel
from matplotlib.widgets import *
import igraph as ig
import matplotlib.pyplot as plt
from Button_click import BClick

if __name__ == '__main__':
    g=excel.pull_from_excel("input.xlsx")
    a=[]
    for i in range(len(g.vs["Etykieta"])):
        a.append(g.vs[i]["Etykieta"]+str(i))
    fig,ax=plt.subplots()
    ig.plot(g,
            target=ax,
            layout="circle",  # print nodes in a circular layout
            vertex_size=0.5,
            vertex_color="steelblue",
            vertex_frame_width=4.0,
            vertex_frame_color="white",
            vertex_label=a,
            edge_label=g.es["Etykieta"],
            vertex_label_size=10,
            edge_label_size=7.0,
            edge_width=2,
            edge_color="#7142cf"
            )
    click=BClick(g)
    ax_box = plt.axes([0.15, 0.05, 0.6, 0.07])
    textbox = TextBox(ax_box, 'Vertices')
    textbox.on_text_change(click.assignVerticles_to_production)
    ax_but1 = plt.axes([0.6, 0.05, 0.7, 0.07])
    button1 = Button(ax_but1, 'P1')
    button1.on_clicked(click.pro1)
    ax_but2 = plt.axes([0.7, 0.05, 0.8, 0.07])
    button2 = Button(ax_but2, 'P2')
    button2.on_clicked(click.pro2)
    plt.show()

