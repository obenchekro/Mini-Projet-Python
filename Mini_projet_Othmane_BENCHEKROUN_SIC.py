#MINI PROJET REALISE PAR OTHMANE BENCHEKROUN 2A INSA EM SIC 
#QUESTION 1
class Graphe(object):
    def __init__ (self, nom, listedenoeuds):
        self.nom = nom
        self.listedenoeuds = listedenoeuds
    def AjoutNoeud(self, noeud): 
        self.listedenoeuds["Noeuds du graphe"].append(noeud)
    def AjoutLiaison(self, noeud, voisin): 
            noeud.AjoutVoisin(voisin.nom)
            voisin.AjoutVoisin(noeud.nom)
    def Affichage(self): 
        print("Graphe :",self.nom)
        for noeud in self.listedenoeuds["Noeuds du graphe"]:
            print(noeud.nom,", voisins :",noeud.listedevoisins)
#QUESTION 2
class Noeud(object):
    def __init__ (self, nom, listedevoisins):
        self.nom = nom
        self.listedevoisins = listedevoisins
    def AjoutVoisin(self, voisin):
            self.listedevoisins.append(voisin)
#QUESTION 3
graphe1 = Graphe("G1",{"Noeuds du graphe":[]})
A= Noeud("A",[])
B= Noeud("B",[])
C= Noeud("C",[])
D= Noeud("D",[])
E= Noeud("E",[])
F= Noeud("F",[])
G= Noeud("G",[])
H= Noeud("H",[])
I= Noeud("I",[])
J= Noeud("J",[])
K= Noeud("K",[])
for noeud in [A,B,C,D,E,F,G,H,I,J,K]:
    graphe1.AjoutNoeud(noeud)
graphe1.AjoutLiaison(A,B)
graphe1.AjoutLiaison(A,E)
graphe1.AjoutLiaison(B,F)
graphe1.AjoutLiaison(C,G)
graphe1.AjoutLiaison(D,E)
graphe1.AjoutLiaison(D,H)
graphe1.AjoutLiaison(E,H)
graphe1.AjoutLiaison(F,G)
graphe1.AjoutLiaison(F,I)
graphe1.AjoutLiaison(F,J)
graphe1.AjoutLiaison(G,J)
graphe1.AjoutLiaison(H,I)
graphe1.Affichage()
