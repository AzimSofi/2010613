import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import time
from networkx.algorithms import tree
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MST Algorithms")
        self.geometry("800x600")

        self.graph = nx.Graph()

        self.edge_entries = [tk.Entry(self) for _ in range(3)]
        tk.Label(self, text="Edges (Node1, Node2, Weight):").grid(column=0, row=0)
        for i, entry in enumerate(self.edge_entries):
            entry.grid(column=i+1, row=0)
        tk.Button(self, text="Add Edge", command=self.add_edge).grid(column=4, row=0)

        tk.Button(self, text="Calculate Kruskal's MST",
                   command=self.calculate_kruskal).grid(column=0, row=1)
        tk.Button(self, text="Calculate Prim's MST",
                   command=self.calculate_prim).grid(column=1, row=1)

        self.quit_button()
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self) 
        self.canvas.get_tk_widget().grid(column=0, row=2,
                                        columnspan=5)

    def quit_button(self):
        # 閉じるボタン
        quit_btn = tk.Button(self)
        quit_btn['text'] = 'Exit (閉じる)'
        quit_btn['command'] = self.quit
        quit_btn.grid(column=2, row=3)    

    def add_edge(self):
        u, v, w = [entry.get() for entry in self.edge_entries]
        self.graph.add_edge(u, v, weight=float(w))
        self.plot_graph(self.graph)

    def calculate_mst(self, algorithm):
        edges_copy = list(self.graph.edges(data=True))  # make a copy of the edges to restore later
        self.graph.clear()
        
        mst_graph = nx.Graph()

        if algorithm == "kruskal":
            self.graph.add_edges_from(edges_copy)
            edges = sorted(self.graph.edges(data=True), key=lambda edge: edge[2]["weight"])
            for edge in edges:
                u, v, w = edge
                # add the edge if it doesn't form a cycle
                if not mst_graph.has_node(v) or (mst_graph.has_node(u) and u not in nx.node_connected_component(mst_graph, v)):
                    mst_graph.add_edge(u, v, weight=w["weight"])  # also copy the weight attribute
                    self.plot_graph(mst_graph)
                    self.canvas.get_tk_widget().update()  # force the widget to update
                    time.sleep(0.5)  # pause for a moment to see the result


        elif algorithm == "prim":
            self.graph.add_edges_from(edges_copy)
            start_node = list(self.graph.nodes())[0]  # select the first node to start
            mst_graph.add_node(start_node)
            while mst_graph.number_of_nodes() < self.graph.number_of_nodes():
                crossing_edges = [(u, v, d) for u, v, d in self.graph.edges(data=True) if ((u in mst_graph.nodes() and v not in mst_graph.nodes()) or (v in mst_graph.nodes() and u not in mst_graph.nodes()))]
                edge_to_add = min(crossing_edges, key=lambda edge: edge[2]["weight"])
                mst_graph.add_edge(edge_to_add[0], edge_to_add[1], weight=edge_to_add[2]["weight"])
                self.plot_graph(mst_graph)
                self.canvas.get_tk_widget().update()  # force the widget to update
                time.sleep(0.5)  # pause for a moment to see the result

        self.graph.clear()
        self.graph.add_edges_from(edges_copy)  # restore the original edges

    def calculate_kruskal(self):
        self.calculate_mst("kruskal")

    def calculate_prim(self):
        self.calculate_mst("prim")

    def plot_graph(self, graph):
        self.figure.clear()
        pos = nx.spring_layout(graph)

        ax = self.figure.add_subplot(111)  # Add a subplot to the figure

        # nodes
        nx.draw_networkx_nodes(graph, pos, node_size=700, ax=ax)

        # edges
        nx.draw_networkx_edges(graph, pos, ax=ax)

        # labels
        edge_labels = nx.get_edge_attributes(graph, 'weight')
        nx.draw_networkx_labels(graph, pos, font_size=20, ax=ax)
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=20, ax=ax)
        
        self.canvas.draw()



if __name__ == "__main__":
    app = Application()
    app.mainloop()
