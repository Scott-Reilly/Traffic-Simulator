import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from([(1,"I1"),(2,"I1"), (3, "I1"), ("I1", "I2"), ("I2", 4), ("I2", 5),("I2", 6)])


def getPath(start, end):
    return nx.shortest_path(G,start,end)

Waypoints = {
    1: [(422,519), (377,520)],
    2: [(247,497), (247,455)],
    3: [(273,321), (316,321)],
    "I2": [(445,327), (445,388)],
    4: [(682,322), (726,322)],
    5: [(857,348), (857,390)],  
    6: [(833,520), (788,520)],
    "I1": [(659,494), (659, 451)]       
}
