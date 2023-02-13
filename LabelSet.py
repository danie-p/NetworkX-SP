import networkx as nx

def NajdiCestu(zVrchola, doVrchola, dataset):
    data = []
    for riadok in open(dataset):
        data.append(riadok.split())

    graf = nx.DiGraph()
    for riadok in data:
        graf.add_edge(eval(riadok[0]), eval(riadok[1]), weight=eval(riadok[2]))
    
    infinity = 100200
    # Krok 1: Inicializácia
    epsilon = [zVrchola]
    
    for i in range (1, len(graf.nodes()) + 1):
        if i == zVrchola:
            graf.nodes[i]['t'] = 0
            graf.nodes[i]['pouzity'] = True
        else:
            graf.nodes[i]['t'] = infinity
            graf.nodes[i]['pouzity'] = False
        graf.nodes[i]['x'] = 0
    
    # Krok 2: Porovnanie
    while(epsilon):
        # Ako prvok r z množiny epsilon vyberáme prvok s najmenšou značkou t
        min_t_epsilon = min(graf.nodes[i]['t'] for i in epsilon)
        min_vrchol = [i for i in epsilon if graf.nodes[i]['t'] == min_t_epsilon]
        r = epsilon[epsilon.index(min_vrchol[0])]
        epsilon.remove(r)
        if r == doVrchola:
            break

        for vystupnaHrana in graf.out_edges(r):
            # vystupnaHrana[1] = koncovy vrchol hrany
            if graf.nodes[vystupnaHrana[1]]['t'] > graf.nodes[r]['t'] + graf.get_edge_data(vystupnaHrana[0], vystupnaHrana[1])['weight']:
                graf.nodes[vystupnaHrana[1]]['t'] = graf.nodes[r]['t'] + graf.get_edge_data(vystupnaHrana[0], vystupnaHrana[1])['weight']
                graf.nodes[vystupnaHrana[1]]['x'] = r
                if not graf.nodes[vystupnaHrana[1]]['pouzity']:
                    epsilon.append(vystupnaHrana[1])
                    graf.nodes[vystupnaHrana[1]]['pouzity'] = True
        # Krok 3: Opakovanie, pokiaľ nie je epsilon prázdny
    return graf

def Vypis(doVrchola, graf):
    return str(graf.nodes[doVrchola]['t'])

def Vypis2(doVrchola, graf):
    i = doVrchola
    cesta = [i]
    while(graf.nodes[i]['x'] != 0):
        i = graf.nodes[i]['x']
        cesta.append(i)
    cesta.reverse()
    string = ""
    for bod in cesta:
        string += str(bod) + " -> "
    return string