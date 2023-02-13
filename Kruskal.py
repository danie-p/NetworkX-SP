import networkx as nx
import matplotlib.pyplot as plt

# ako parameter očakáva hodnotu True (najdrahšie kostra) alebo False (najlacnejšia kostra)
def KruskalI(param, dataset):
    data = []
    for riadok in open(dataset):
        data.append(riadok.split())

    graf = nx.Graph()
    for riadok in data:
        graf.add_edge(eval(riadok[0]), eval(riadok[1]), weight=eval(riadok[2]))
    kostra = nx.Graph()

    # Krok 1: Zoradenie hrán podľa ohodnotenia do postupnosti P
    P = sorted(graf.edges(data=True), key=lambda x: x[2].get('weight', 1), reverse=param)
        
    while((kostra.number_of_edges() != graf.number_of_nodes() - 1) and (P)):
        # Krok 2: Ak hrana vybraná z postupnosti P nevytvára s ostatnými hranami kostry cyklus, zaradíme ju do kostry
        kostra.add_edge(P[0][0], P[0][1], weight=graf.get_edge_data(P[0][0], P[0][1])['weight'])
        
        try:
            nx.find_cycle(kostra)
        except nx.exception.NetworkXNoCycle:
            pass
        else:
            kostra.remove_edge(P[0][0], P[0][1])

        P.remove(P[0])
        
        #Krok 3: Opakovanie, pokiaľ nie je počet hrán kostry rovný počtu vrcholov digrafu - 1 alebo pokiaľ nie je postupnosť P prázdna
    
    nx.draw_planar(kostra, node_size=20)
    plt.savefig("obrazok.png", facecolor='#b3f4dd', transparent=True)
    plt.clf()

    return kostra
    
def KruskalII(param, dataset):
    data = []
    for riadok in open(dataset):
        data.append(riadok.split())

    graf = nx.Graph()
    for riadok in data:
        graf.add_edge(eval(riadok[0]), eval(riadok[1]), weight=eval(riadok[2]))

    kostra = nx.Graph()
    
    # Krok 1: Zoradenie hrán podľa ohodnotenia do postupnosti P
    P = sorted(graf.edges(data=True), key=lambda x: x[2].get('weight', 1), reverse=param)

    # Krok 2: Označenie vrcholov
    for i in range (1, len(graf.nodes()) + 1):
        graf.nodes[i]['k'] = i

    while((kostra.number_of_edges() != graf.number_of_nodes() - 1) and (P)):
        # Krok 3: Zaradenie vyhovujúcej hrany do kostry
        k0 = graf.nodes[P[0][0]]['k']
        k1 = graf.nodes[P[0][1]]['k']
        if k0 != k1:
            kostra.add_edge(P[0][0], P[0][1], weight=graf.get_edge_data(P[0][0], P[0][1])['weight'])
            kmin = min(k0, k1)
            kmax = max(k0, k1)
            for i in range (1, len(graf.nodes()) + 1):
                if graf.nodes[i]['k'] == kmax:
                        graf.nodes[i]['k'] = kmin
        P.remove(P[0])

        # Krok 3: Opakovanie

    nx.draw_planar(kostra, node_size=20)
    plt.savefig("obrazok.png", facecolor='#b3f4dd', transparent=True)
    plt.clf()
    
    return kostra

def Vypis(kostra):
    return str(sum(kostra.get_edge_data(hrana[0], hrana[1])['weight'] for hrana in kostra.edges()))