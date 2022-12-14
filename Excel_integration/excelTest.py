# Testy modułu excelowego.
# Jak chcecie jednostkowe to zmontuję jakieś, póki co są "na oko"
# Tj. robicie excela w tej ścieżce co  tam macie z takim grafem jaki chcecie.
# oczywiście zgodnie z ExcelFormatting.md
# program wam pokaże ten graf - kurtuazja matplotlib.pypylot
# a potem zapisze do testfakeexcelresults.xlsx.
# Jeżeli graf wygląda jak powinien i zapisuje sie to samo co sie wczytało to jest OK.
# Jak sie sypie to mnie wzywać (Polokratos/Piotr Koproń)
import excel
import igraph as omg
import matplotlib.pyplot as plt # do pokazywania grafów w konsoli

G = excel.pull_from_excel("testfakeexcel.xlsx")

#Coś rysuje, przekopiowane* z quickstarta to igraph
fig, ax = plt.subplots(figsize=(5,5))
omg.plot(
    G,
    target=ax,
    layout="circle", # print nodes in a circular layout
    vertex_size=0.1,
    vertex_color="steelblue",
    vertex_frame_width=4.0,
    vertex_frame_color="white",
    vertex_label=G.vs["Etykieta"],
    edge_label=G.es["Etykieta"],
    vertex_label_size=7.0,
    edge_label_size=7.0,
    edge_width=2,
    edge_color="#7142cf")

plt.show() # Pokazuje na ekranie żeby debug można było robić


excel.push_to_excel(G,"Excel_integration\\testfakeexcel.xlsx")