import tkinter as tk
from recruitment import query_conceptnet, find_strongest_relationship
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Nesne İlişkileri Haritası")

def draw_graph():
    G = nx.Graph()

    nesneler = ['computer', 'keyboard', 'chair', 'office', 'desk', 'stapler']

    G.add_edge('Computer', 'Keyboard', relation='AtLocation')
    G.add_edge('Chair', 'Office', relation='AtLocation')
    G.add_edge('Desk', 'Stapler', relation='PartOf')

    pos1 = {'Computer': [-2, 2], 'Keyboard': [2, 2]}
    pos2 = {'Chair': [-2, 0], 'Office': [2, 0]}
    pos3 = {'Desk': [-2, -2], 'Stapler': [2, -2]}

    pos = {**pos1, **pos2, **pos3}

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw_networkx_nodes(G, pos, node_size=3000, node_color='skyblue', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold', ax=ax)
    nx.draw_networkx_edges(G, pos, width=2, edge_color='black', ax=ax)

    edge_labels = nx.get_edge_attributes(G, 'relation')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, ax=ax)

    plt.text(0, 1.6, "İşlevsel İlişki", horizontalalignment='center', fontsize=12)
    plt.text(0, 0.2, "Konumsal İlişki", horizontalalignment='center', fontsize=12)
    plt.text(0, -1.8, "Konumsal İlişki", horizontalalignment='center', fontsize=12)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

button = tk.Button(root, text="Nesne İlişkilerini Göster", command=draw_graph)
button.pack()

root.mainloop()
