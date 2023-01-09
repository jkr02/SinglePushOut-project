import matplotlib.text
from Excel_integration import excel
from matplotlib.widgets import *
import igraph as ig
import matplotlib.pyplot as plt
from Button_click import BClick

def button_click(event):
    label = event.inaxes.texts[0].get_text()
    a = productions[label]()
    ax.clear()
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
    fig.canvas.draw_idle()

if __name__ == '__main__':
    g = excel.pull_from_excel("input.xlsx")
    a = []
    for i in range(len(g.vs["Etykieta"])):
        a.append(g.vs[i]["Etykieta"] + " " + str(i))
    fig, ax = plt.subplots()
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

    click = BClick(g)

    productions = {
        'P1': click.pro1,
        'P2': click.pro2,
        'P3': click.pro3,
        'P4': click.pro4,
        'P5': click.pro5,
        'P6': click.pro6,
        'P7': click.pro7,
        'P8': click.pro8,
        'P9': click.pro9,
        'P10': click.pro10
    }

    ax_box = fig.add_axes([0.12, 0.05, 0.3, 0.075])
    textbox = TextBox(ax_box, 'Vertices')
    textbox.on_text_change(click.assignVerticles_to_production)

    ax_but1 = fig.add_axes([0.4, 0.05, 0.06, 0.075])
    button1 = Button(ax_but1, 'P1',)

    button1.on_clicked(button_click)

    ax_but2 = fig.add_axes([0.46, 0.05, 0.06, 0.075])
    button2 = Button(ax_but2, 'P2')
    button2.on_clicked(button_click)

    ax_but3 = fig.add_axes([0.52, 0.05, 0.06, 0.075])
    button3 = Button(ax_but3, 'P3')
    button3.on_clicked(button_click)

    ax_but4 = fig.add_axes([0.58, 0.05, 0.06, 0.075])
    button4 = Button(ax_but4, 'P4')
    button4.on_clicked(button_click)

    ax_but5 = fig.add_axes([0.64, 0.05, 0.06, 0.075])
    button5 = Button(ax_but5, 'P5')
    button5.on_clicked(button_click)

    ax_but6 = fig.add_axes([0.70, 0.05, 0.06, 0.075])
    button6 = Button(ax_but6, 'P6')
    button6.on_clicked(button_click)

    ax_but7 = fig.add_axes([0.76, 0.05, 0.06, 0.075])
    button7 = Button(ax_but7, 'P7')
    button7.on_clicked(button_click)

    ax_but8 = fig.add_axes([0.82, 0.05, 0.06, 0.075])
    button8 = Button(ax_but8, 'P8')
    button8.on_clicked(button_click)

    ax_but9 = fig.add_axes([0.88, 0.05, 0.06, 0.075])
    button9 = Button(ax_but9, 'P9')
    button9.on_clicked(button_click)

    ax_but10 = fig.add_axes([0.94, 0.05, 0.06, 0.075])
    button10 = Button(ax_but10, 'P10')
    button10.on_clicked(button_click)

    ax_but11 = fig.add_axes([0, 0.924, 0.15, 0.075])
    button11 = Button(ax_but11, 'Save graph')
    button11.on_clicked(click.pushGraph_to_excel)

    plt.show()
