
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

G.add_node("charvik")
G.add_node("sushma")
G.add_node("venky")
G.add_node("charan")

G.add_edge("charvik", "sushma")
G.add_edge("sushma", "venky")
G.add_edge("venky", "charan")
G.add_edge("charan", "charvik")

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray")

nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

plt.axis("off")
plt.show()
