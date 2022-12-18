import igraph as omg
import pandas as panda
#TODO: Testy tego jakieś chcecie?

#Parametry:
# Path to ścieżka do excela
# sheet to który arkusz brać. 
# Domyślnie Sheet1 bo jak otwieracie nowego excela to tak sie nazywa pierwszy arkusz
# Jeżeli zagwarantujecie mu że będzie tylko jeden arkusz w pliku
# to możecie dawać None i zrozumie.
# label to jaką nazwę chcecie mieć na etykiety. Domyślnie Etykieta.

# Zwraca:
# graph z igrapha.
def pull_from_excel(path : str, sheet: str = "Sheet1", label:str = "Etykieta") -> omg.Graph:
    dataframe: panda.DataFrame = panda.read_excel(path,sheet,header=0,dtype="str").fillna('')#w 0 mamy etykiety dla grafów.
    #Akurat tutaj lista2D jest wygodna do powyciągania tego 
    verticeNames = dataframe.columns
    matrix = dataframe.to_numpy().tolist()
    
    for i in range(len(matrix)): #czyszczenie przekatnej głównej
        matrix[i][i] = ''
    
    #Konstrukcja grafu
    G = omg.Graph.Adjacency(atoi_Matrix(matrix)) #igaph chce numerki a nie napisy to macierzy
    #Aplikacja etykiet
    G.vs[label] = verticeNames
    applyEdgeLabels(G,matrix,label)
    
    
    return G # macie graf bawcie sie dobrze.


#Parametry:
# Path to ścieżka gdzie chcecie to zapisać, domyślnie "tmp.xlsx" w katalogu roboczym. 
# (A potem szukajcie a znajdziecie)
# G to graf.
# label to string jak nazwaliście etykiety. Domyślnie "Etykieta"
def push_to_excel(G: omg.Graph, path:str = "tmp.xlsx", label:str = "Etykieta")->None:
   verticeNames = G.vs[label]
   matrix = get_formatted_adjacency(G)
   
   df = panda.DataFrame(data= matrix, columns=verticeNames)
   df.to_excel(excel_writer = path, index=False)


# Funkcje pomocnicze. Możecie spokojnie ignorować.
# Albo nie. Nie jestem Waszą matką.
def atoi_Matrix(matrix :list[list[str]]): # zamienia etykiety na numerki.
    return [[ 0 if j=='' else 1 for j in i] for i in matrix]
    
def applyEdgeLabels(G: omg.Graph, matrix: list[list[str]],labelstr:str):
    labels = ['' for _ in range(G.ecount())]
    for edge_index in range(len(G.es)):
        source = G.es[edge_index].source
        target = G.es[edge_index].target
        label = matrix[source][target]
        print(label)
        labels[edge_index] = label
    G.es[labelstr] = labels

def get_formatted_adjacency(G: omg.Graph): 
    matrix = [[ '' for i in range(G.vcount())] for _ in range(G.vcount())]
    for e in G.es:
        sourceLabel = G.vs[e.source]
        targetLabel = G.vs[e.target]
        
        
    return 'x'
    

