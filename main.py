from Excel_integration import excel
from matplotlib.widgets import *
import igraph as ig
import matplotlib.pyplot as plt
from Button_click import BClick

if __name__ == '__main__':
    g=excel.pull_from_excel("input.xlsx")
    a=[]
    for i in range(len(g.vs["Etykieta"])):
        a.append(g.vs[i]["Etykieta"]+ " "+ str(i))
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
    ax_box = plt.axes([0.15, 0.05, 0.5, 0.07])
    textbox = TextBox(ax_box, 'Vertices')
    textbox.on_text_change(click.assignVerticles_to_production)

    ax_but1 = plt.axes([0.5, 0.05, 0.55, 0.07])
    button1 = Button(ax_but1, 'P1')
    button1.on_clicked(click.pro1)

    ax_but2 = plt.axes([0.55, 0.05, 0.6, 0.07])
    button2 = Button(ax_but2, 'P2')
    button2.on_clicked(click.pro2)

    ax_but3 = plt.axes([0.6, 0.05, 0.65, 0.07])
    button3 = Button(ax_but3, 'P3')
    button3.on_clicked(click.pro3)

    ax_but4 = plt.axes([0.65, 0.05, 0.7, 0.07])
    button4 = Button(ax_but4, 'P4')
    button4.on_clicked(click.pro4)

    ax_but5 = plt.axes([0.7, 0.05, 0.75, 0.07])
    button5 = Button(ax_but5, 'P5')
    button5.on_clicked(click.pro5)

    ax_but6 = plt.axes([0.75, 0.05, 0.8, 0.07])
    button6 = Button(ax_but6, 'P6')
    button6.on_clicked(click.pro6)

    ax_but7 = plt.axes([0.8, 0.05, 0.85, 0.07])
    button7 = Button(ax_but7, 'P7')
    button7.on_clicked(click.pro7)

    ax_but8 = plt.axes([0.85, 0.05, 0.9, 0.07])
    button8 = Button(ax_but8, 'P8')
    button8.on_clicked(click.pro8)

    ax_but9 = plt.axes([0.9, 0.05, 0.95, 0.07])
    button9 = Button(ax_but9, 'P9')
    button9.on_clicked(click.pro9)

    ax_but10 = plt.axes([0.95, 0.05, 1, 0.07])
    button10 = Button(ax_but10, 'P10')
    button10.on_clicked(click.pro10)
    plt.show()

