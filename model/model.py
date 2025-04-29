import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.aeroporti = DAO.getAllAeroporti()
        self.idMap_aeroporti = {}
        for a in self.aeroporti:
            self.idMap_aeroporti[a.ID] = a

    def buildGraph(self, x):
        grafo = nx.Graph()
        elencoArchi = DAO.getEdges(x)
        for edge in elencoArchi:
            aeroportoP = self.idMap_aeroporti[edge[0]]
            aeroportoA = self.idMap_aeroporti[edge[1]]
            distanza_media = edge[2]
            grafo.add_edge(aeroportoP, aeroportoA, weight=distanza_media)
        return len(grafo.nodes), len(grafo.edges), grafo


