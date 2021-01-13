from typing import List

from ex3.src import GraphInterface
from ex3.src.DiGraph import DiGraph
from ex3.src.GraphAlgoInterface import GraphAlgoInterface
import json

import heapq
import queue
import math
import numpy as np
import matplotlib.pyplot as plt
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph
        self.string = "Graph"

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        self.string = file_name
        vertex = {}
        edges = {}
        try:
            with open(file_name, "r") as file:
                new_graph_dict = json.load(file)
                vertex = new_graph_dict["Nodes"]
                edges = new_graph_dict["Edges"]
                self.graph = DiGraph()
                for i in vertex:
                    if "pos" not in i:
                        i["pos"] = None
                    self.graph.add_node(i["id"], i["pos"])
                for e in edges:
                    self.graph.add_edge(e["src"], e["dest"], e["w"])

        except IOError as e:
            print(e)

            return False

        return True

    def save_to_json(self, file_name: str) -> bool:
        vertex = []
        edges = []
        graph = {}
        for i in self.graph.get_all_v():
            n = {"pos": i.pos, "id": i.key}
            vertex.append(n)
            for j in self.graph.all_out_edges_of_node(i.key).values():
                e = {"src": i.key, "w": j.weight, "dest": j.dst}
                edges.append(e)

        graph["Edges"] = edges
        graph["Nodes"] = vertex

        try:
            with open(file_name, "w") as file:
                json.dump(graph, indent=4, fp=file)

        except IOError as e:
            print(e)

            return False

        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.Nodes.keys() or id2 not in self.graph.Nodes.keys():
            return float('infinity'), []
        self.Dijkstra(id1)
        ls = []
        if self.graph.Nodes.get(id2).tag == float('infinity'):
            return float('infinity'), ls
        form = id2
        ls.append(form)
        while id1 not in ls:
            ls.append(self.graph.Nodes.get(form).r_from.key)
            form = self.graph.Nodes.get(form).r_from.key
        ls.reverse()
        return self.graph.Nodes.get(id2).tag, ls

    def connected_component(self, id1: int):
        if id1 not in self.graph.Nodes.keys() or self.graph is None:
            return []
        l_ist = self.Kosaraju(id1)
        return l_ist

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        l_ist = []
        al_inScc = []
        for i in self.graph.Nodes.values():
            if i.key not in al_inScc:
                l = self.Kosaraju(i.key)
                for k in l:
                    al_inScc.append(k)
                l_ist.append(l)
        return l_ist

    def plot_graph(self) -> None:
        plt.title(self.string)
        x_vals = []
        y_vals = []
        for xy in self.graph.Nodes.values():
            if xy.pos is None:
                xy.pos = (random.randrange(0, 100), random.randrange(0, 100), 0)
                x_vals.append(xy.pos[0])
                y_vals.append(xy.pos[1])
            else:
                string = xy.pos.split(',')
                xy.pos = tuple(string)
                x_vals.append(float(string[0]))
                y_vals.append(float(string[1]))

        plt.plot(x_vals, y_vals, 'o')
        for v in self.graph.Nodes.values():
            v_x = float(v.pos[0])
            v_y = float(v.pos[1])
            plt.annotate(v.key, (v_x - 0.00015, v_y + 0.00015), color='red')
            for e in self.graph.EdgesSrc[v.key].values():
                x_e = float(self.graph.Nodes[e.dst].pos[0])
                y_e = float(self.graph.Nodes[e.dst].pos[1])

                plt.arrow(v_x, v_y, x_e - v_x, y_e - v_y, length_includes_head=True, head_width=0.0001991599,
                          width=0.0000005, color='blue')

        plt.show()

    def Dijkstra(self, src):
        for vertex in self.graph.Nodes.values():
            vertex.tag = float('infinity')
        self.graph.Nodes.get(src).tag = 0
        pq = [self.graph.Nodes.get(src)]
        visited = [src]
        while len(pq) > 0:
            node = pq.pop(0)
            for neighbor in self.graph.EdgesSrc[node.key].values():
                weight = node.tag + neighbor.weight
                if weight < self.graph.Nodes.get(neighbor.dst).tag:
                    self.graph.Nodes.get(neighbor.dst).tag = weight
                    self.graph.Nodes.get(neighbor.dst).r_from = node
                    if neighbor.dst not in visited:
                        pq.append(self.graph.Nodes.get(neighbor.dst))
                        visited.append(neighbor.dst)

        return

    def Kosaraju(self, src):
        s = [src]
        visited = {}
        while len(s) > 0:  # DFS Graph
            v = s.pop()
            if v not in visited.keys():
                visited[v] = self.graph.Nodes[v]
                for edge in self.graph.EdgesSrc[v].values():
                    s.append(edge.dst)
        visited_2 = {}
        s_2 = [src]
        while len(s_2) > 0:
            v = s_2.pop()
            if v not in visited_2.keys():
                visited_2[v] = self.graph.Nodes[v]
                for edge in self.graph.EdgesDst[v].values():
                    s_2.append(edge.dst)

        x = set(visited).intersection(visited_2)
        return list(x)
