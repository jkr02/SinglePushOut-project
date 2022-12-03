import igraph as omg
import pandas as panda
#TODO: Testy tego jakieś chcecie?

#Parametry:
# Path to ścieżka do excela
# sheet to który arkusz brać. 
# Domyślnie Sheet1 bo jak otwieracie nowego excela to tak sie nazywa pierwszy arkusz
# Jeżeli zagwarantujecie mu że będzie tylko jeden arkusz w pliku
# to możecie dawać None i zrozumie.

# Zwraca:
# graph z igrapha.
def pull_from_excel(path : str, sheet: str = "Sheet1") -> omg.Graph:
    dataframe: panda.DataFrame = panda.read_excel(path,sheet,header=0)#w 0 mamy etykiety dla grafów.
    #Akurat tutaj lista2D jest wygodna do powyciągania tego 
    verticeNames = dataframe.columns
    matrix = dataframe.to_numpy().tolist()
    #Konstrukcja grafu
    G = omg.Graph.Adjacency(matrix)
    #Aplikacja etykiet
    G.vs["Etykieta"] = verticeNames
    
    return G # macie graf bawcie sie dobrze.


#Parametry:
# Path to ścieżka gdzie chcecie to zapisać, domyślnie "tmp.xlsx" w katalogu roboczym. 
# (A potem szukajcie a znajdziecie)
# G to graf.
def push_to_excel(G: omg.Graph, path:str = "tmp.xlsx")->None:
   verticeNames = G.vs["Etykieta"]
   matrix = G.get_adjacency()
   df = panda.DataFrame(data= matrix, columns=verticeNames)
   df.to_excel(excel_writer = path, index=False)
   