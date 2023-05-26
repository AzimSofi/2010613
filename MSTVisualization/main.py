import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import tree
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("MST Algorithms")
        self.geometry("800x600")

        self.graph = nx.Graph()

        self.edge_entries = [tk.Entry(self) for _ in range(3)]
        tk.Label(self, text="Edges (Node1, Node2, Weight):").grid(column=0, row=0)
        for i, entry in enumerate(self.edge_entries):
            entry.grid(column=i+1, row=0)
        tk.Button(self, text="Add Edge", command=self.add_edge).grid(column=4, row=0)

        tk.Button(self, text="Calculate Kruskal's MST", command=self.calculate_kruskal).grid(column=0, row=1)
        tk.Button(self, text="Calculate Prim's MST", command=self.calculate_prim).grid(column=1, row=1)

        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self) 
        self.canvas.get_tk_widget().grid(column=0, row=2, columnspan=5)

    def add_edge(self):
        u, v, w = [entry.get() for entry in self.edge_entries]
        self.graph.add_edge(u, v, weight=float(w))
        self.plot_graph(self.graph)

    def calculate_mst(self, algorithm):
        edges_copy = list(self.graph.edges(data=True))  # make a copy of the edges to restore later
        self.graph.clear()
        if algorithm == "kruskal":
            self.graph.add_edges_from(edges_copy)
            mst = tree.minimum_spanning_edges(self.graph, algorithm='kruskal', data=True)
        elif algorithm == "prim":
            self.graph.add_edges_from(edges_copy)
            mst = tree.minimum_spanning_edges(self.graph, algorithm='prim', data=True)
        mst_graph = nx.Graph()
        mst_graph.add_edges_from(mst)
        self.plot_graph(mst_graph)
        self.graph.clear()
        self.graph.add_edges_from(edges_copy)  # restore the original edges

    def calculate_kruskal(self):
        self.calculate_mst("kruskal")

    def calculate_prim(self):
        self.calculate_mst("prim")

    def plot_graph(self, graph):
        self.figure.clear()
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, ax=self.figure.add_subplot(111))
        labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
        self.canvas.draw()


if __name__ == "__main__":
    app = Application()
    app.mainloop()
