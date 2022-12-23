# Standardy formatowania excela

*Czyli jak excele mają wyglądać.*

Zgodnie z ustaleniami z prof. Kotulskim:

Reprezentujemy graf *macierzą sąsiedztwa.*

W wierszu 1 zapisujemy ekytkiety wierzchołków - czyli czy wierzchołek jest A,B, czy C.

Np. w A1 zapisujemy etykiete wierzchołka 1, w B1 etykiete wierzcholka 2 etc.
*W etykietach wierzchołków kropka '.' jest zakazana. (Usunie Wam kropke i wszystko po kropce)*
Wiersze 2+ służą do zapisywania relacji miedzy wierzchołkami (krawędzi)
*Pusty string oznacza brak krawędzi, cokolwiek innego jest etykietą krawędzi*
**Na przekątnej głównej dane są ignorowane. Jednkowoż należy jakąś dummy wartość ('X' wystarczy) wstawić (przynajmniej na ostatni wierzchołek żeby numpy wiedział ile wierszy pobrać**

Np. w A3 będzie informacja o krawędzi między wierzchołkiem 1 i 2.

w A4 -> między 1 i 3

w B4 -> między 2 a 4.

zauważyć, że tutaj tablice zaczynają się od **2**. Ponieważ gdyż Excel sam z siebie zaczyna tablice od 1 *oraz* 1 wiersz idzie na etykiety wierzchołków.

Poniżej przekątnej głównej dane są ignorowane i guess.
