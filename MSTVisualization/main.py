import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import time, random, string
from networkx.algorithms import tree
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("MST Algorithms")
        self.geometry("900x850")
        self.minsize(900, 850)  # Set minimum window size to prevent hiding buttons
        self.graph = nx.Graph()
        
        # Edge input frame
        edge_frame = tk.Frame(self)
        edge_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        tk.Label(edge_frame, text="Edges: ").grid(column=0, row=0)
        
        placeholders = ["Node 1", "Node 2", "Weight"]
        self.edge_entries = [self.create_placeholder_entry(edge_frame, text) for text in placeholders]
        for i, entry in enumerate(self.edge_entries):
            entry.grid(column=i+1, row=0)
        tk.Button(edge_frame, text="Add Edge", command=self.add_edge).grid(column=4, row=0)

        # Random graph generation frame
        random_frame = tk.Frame(self)
        random_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        tk.Button(random_frame, text="Generate a random graph", command=self.generate_random_graph_letter).grid(column=0, row=0)
        tk.Button(random_frame, text="Generate a random Japanese route", command=self.generate_random_graph_japanese).grid(column=1, row=0)
        
        # MST calculation and graph connectivity indicator frame
        mst_and_indicator_frame = tk.Frame(self)
        mst_and_indicator_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        # MST calculation frame
        mst_frame = tk.Frame(mst_and_indicator_frame)
        mst_frame.grid(row=0, column=0, sticky="ew")
        self.mst_kruskal_button = tk.Button(mst_frame, text="Calculate Kruskal's MST", command=self.calculate_kruskal)
        self.mst_kruskal_button.grid(column=0, row=0)
        self.mst_prim_button = tk.Button(mst_frame, text="Calculate Prim's MST", command=self.calculate_prim)
        self.mst_prim_button.grid(column=1, row=0)

        # Graph connectivity indicator
        self.graph_indicator = tk.StringVar()
        self.graph_indicator.set("Connected: ❌")
        self.graph_indicator_label = tk.Label(mst_and_indicator_frame, textvariable=self.graph_indicator)
        self.graph_indicator_label.grid(row=0, column=1)
        
        # Graph canvas
        self.figure = plt.Figure(figsize=(8, 8), dpi=100)  # Increased figsize
        self.canvas = FigureCanvasTkAgg(self.figure, master=self) 
        self.canvas.get_tk_widget().grid(row=4, column=0,  # Change the row to 4
                                         columnspan=5, sticky="nsew")  # Use sticky="nsew" to allow expansion

        # Control frame
        control_frame = tk.Frame(self)
        control_frame.grid(row=5, column=0, padx=10, pady=10)
        tk.Button(control_frame, text="Reset graph", command=self.clear_graph).grid(row=0, column=0, padx=20)  # Add padx to add padding between buttons
        tk.Button(control_frame, text="Exit (閉じる)", command=self.quit).grid(row=0, column=1, padx=20)

        # Configure grid layout
        self.grid_rowconfigure(4, weight=1)  # Set higher weight to row 4
        self.grid_columnconfigure(0, weight=1, minsize=200)  # Set higher weight and minsize to column 0
        control_frame.columnconfigure(0, weight=1)  # Center the buttons by expanding the columns in control_frame
        control_frame.columnconfigure(1, weight=1)
        control_frame.columnconfigure(2, weight=1)
        
        # Update connectivity indicator
        self.update_graph_indicator()

    # 作成済みグラフ
    def random_graph(self, things_to_random):
        
        MAX_NODE = 8
        MIN_NODE = 4
        japan_city_names = [
        "Tokyo", "Yokohama", "Osaka", "Nagoya", "Sapporo", "Fukuoka", "Kobe", "Kyoto",
        "Kawasaki", "Saitama", "Hiroshima", "Sendai", "Kitakyushu", "Chiba", "Sakai",
        "Shizuoka", "Nerima", "Okayama", "Hamamatsu", "Nishinomiya", "Kurashiki", "Kumamoto",
        "Hachioji", "Matsuyama", "Funabashi", "Kagoshima", "Niigata", "Higashihiroshima",
        "Himeji", "Matsudo", "Nagano", "Toyohashi", "Toyota", "Saga", "Utsunomiya", "Oita",
        "Matsue", "Kanazawa", "Kawaguchi", "Ichikawa", "Kurume", "Fukushima", "Asahikawa",
        "Amagasaki", "Yokosuka", "Toyonaka", "Kochi", "Takatsuki", "Akita", "Koshigaya",
        "Miyazaki", "Naha", "Kasugai", "Otsu", "Akashi", "Hirakata", "Fukuyama", "Yamagata",
        "Morioka", "Maebashi", "Kawagoe", "Ichinomiya", "Yokkaichi", "Koshigoe", "Gifu",
        "Nara", "Yamaguchi", "Shimonoseki", "Okazaki", "Kurashiki", "Iwaki", "Hiratsuka",
        "Fujisawa", "Hachinohe", "Kure", "Urayasu", "Kakogawa", "Hakodate", "Kamakura",
        "Ebetsu", "Chigasaki", "Sasebo", "Hoya", "Yao", "Kashihara", "Ibaraki", "Takasaki",
        "Kawasaki", "Ichihara", "Neyagawa", "Ageo", "Akita", "Oyama", "Kasukabe", "Takahashi"]

        self.graph.clear()  # clear the current graph
        n_nodes = random.randint(MIN_NODE, MAX_NODE)  # generate a random number of nodes between MIN_NODE and MAX_NODE

        if things_to_random == 'letter':
            # generate a list of unique random letters from a to o
            nodes = random.sample(string.ascii_uppercase[:15], n_nodes)
        elif things_to_random == 'japan_city_names':
            nodes = random.sample(japan_city_names, n_nodes)

        while True:
            self.graph.clear()
            for node in nodes:
                self.graph.add_node(node)  # add the nodes to the graph

            # ensure the graph is connected
            for i in range(n_nodes-1):
                self.graph.add_edge(nodes[i], nodes[i+1], weight=random.randint(1, 10))  # randomly assign weights between 1 and 10

            # add some extra random edges to make the graph more interesting
            extra_edges = random.randint(1, n_nodes)  # generate a random number of extra edges
            for _ in range(extra_edges):
                node1, node2 = random.sample(nodes, 2)  # select two random nodes
                if node1 != node2 and not self.graph.has_edge(node1, node2):  # ensure we don't connect a node to itself or duplicate edges
                    self.graph.add_edge(node1, node2, weight=random.randint(1, 10))  # add the edge with a random weight
            
            # if the graph is fully connected, break the loop, else generate a new graph
            if nx.is_connected(self.graph):
                break
        self.plot_graph(self.graph)  # display the random graph
        self.update_graph_indicator()

    def calculate_mst(self, algorithm):
        edges_copy = list(self.graph.edges(data=True))  # make a copy of the edges to restore later
        self.graph.clear()

        mst_graph = nx.Graph()

        if algorithm == "kruskal":
            self.graph.add_edges_from(edges_copy)
            edges = sorted(self.graph.edges(data=True), key=lambda edge: edge[2]["weight"])
            for edge in edges:
                u, v, w = edge
                # only add the edge if it doesn't form a cycle
                if not self.would_form_cycle(mst_graph, (u, v)):
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
        self.update_graph_indicator()

    def clear_graph(self):
        self.graph.clear()
        self.plot_graph(self.graph)
        self.update_graph_indicator()
    #
    def add_edge(self):
        u, v, w = [entry.get() for entry in self.edge_entries]
        self.graph.add_edge(u, v, weight=float(w))
        self.plot_graph(self.graph)
        self.update_graph_indicator()  # Update the graph indicator and buttons
       
    def generate_random_graph_letter(self):
        self.random_graph('letter')

    def generate_random_graph_japanese(self):
        self.random_graph('japan_city_names')    

    def would_form_cycle(self, G, edge):
        u, v = edge
        if u in G.nodes and v in G.nodes:
            if u in nx.node_connected_component(G, v):
                return True
        return False

    def calculate_kruskal(self):
        self.calculate_mst("kruskal")

    def calculate_prim(self):
        self.calculate_mst("prim")

    def plot_graph(self, graph):
        self.figure.clear()
        pos = nx.spring_layout(graph, weight="weight", scale=10)

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

    def update_graph_indicator(self):
        if nx.is_empty(self.graph) or not nx.is_connected(self.graph):
            self.graph_indicator.set("Connected: ❌")
        else:
            self.graph_indicator.set("Connected: ✔️")

        self.enable_disable_buttons()

    def enable_disable_buttons(self):
        state = tk.NORMAL if self.is_graph_valid() else tk.DISABLED
        self.mst_kruskal_button.config(state=state)
        self.mst_prim_button.config(state=state)

    def is_graph_valid(self):
        return not nx.is_empty(self.graph) and nx.is_connected(self.graph)

    def create_placeholder_entry(self, parent, placeholder):
        entry = tk.Entry(parent)
        entry.insert(0, placeholder)
        entry['fg'] = 'gray'
        entry.bind("<FocusIn>", lambda event: self.clear_placeholder_text(event, placeholder))
        entry.bind("<FocusOut>", lambda event: self.add_placeholder_text(event, placeholder))
        return entry

    def clear_placeholder_text(self, event, placeholder):
        widget = event.widget
        if widget.get() == placeholder:
            widget.delete(0, tk.END)
            widget['fg'] = 'black'

    def add_placeholder_text(self, event, placeholder):
        widget = event.widget
        if widget.get() == '':
            widget.insert(0, placeholder)
            widget['fg'] = 'gray'

# スクリプトが直接実行された場合にアプリケーションを実行します
if __name__ == "__main__":
    app = Application()
    app.mainloop()
