# Directed Weighted Graph in Python


In this project we implement a weighted directed graph.
After we implement the graph at Python, we compared it vs NetworkX and Java implementation.
The results are in [Wiki](https://github.com/SolomonWirter/Ex3OOP/wiki).

This Project represent 2 main classes:


**class DiGraph:**


The graph build from vertices and edges. Each vertex has key and pos(x, y, z), and each edge has src, dest and weight.
The graph represented by three dictionaries:
* dict of all vertices
* dict of all edges from src vertex
* dict of all edges to src vertex from the dest vertices


* To add an edge to the graph use `add_edge(self, id1: int, id2: int, weight: float)`. Complexity - O(1)
* To add a node to the graph use `add_node(self, node_id: int, pos: tuple = None)`. Complexity - O(1)
* To remove an edge from the graph use `remove_edge(self, node_id1: int, node_id2: int)`. Complexity - O(1)
* To remove a node from the graph use `remove_node(self, node_id: int)`. Complexity - O(E)
* `get_all_v(self)` - return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data). Complexity - O(1)
* `all_in_edges_of_node` - return a dictionary of all the nodes connected to (into) node_id, each node is represented using a pair (other_node_id, weight). Complexity - O(1)
* `all_out_edges_of_node` - return a dictionary of all the nodes connected from node_id, each node is represented using a pair (other_node_id, weight). Complexity - O(1)
* `v_size` - returns the number of vertices in this graph. Complexity - O(1)
* `e_size` - returns the number of edges in this graph. Complexity - O(1)
* `get_mc` - return the current version of this graph. Complexity - O(1)


**class GraphAlgo:**


* For applying any method on a graph first use `__init__(self, graph: DiGraph = DiGraph())` to initiate the graph of the class.

* If you are not sure which Graph you working on use `get_graph(self)` -> weighted_graph.

* save\load weighted_graph is possible `save_to_json(self, file_name: str)` ; `load_from_json(self, file_name: str)` -> both methods return boolean value for success or not. Complexity - O(V+E)

* There are methods for receiving the Shortest Path `shortest_path(self, id1: int, id2: int)` - returns tuple(float, list). This method using Dijkstra algorithm. Complexity - O(V+E)
  >Explanation: *Dijkstra Algorithm* 
  > * Works Similar to *BFS* instead of counting of many Vertices are form 
  > * Source Vertex The Dijkstra Calculate the weight of 
  > * the edges from the Source Vertex - and return 
  > * the Min Sum for each reachable Vertex.

* For finding the SCC of certain node `connected_component(self, id1: int)` - return the list of nodes in the SCC. This method using *Kosaraju's algorithm*. Complexity - O(V+E)

* For finding all SCC in the graph `connected_components(self)` - return the list of all SCC lists. This method using *Kosaraju's algorithm*. Complexity - O(V*(V+E))
  >Explanation: *Kosaraju's Algorithm* (Different Implementation)
  > * Using *DFS Algorithm* first on the graph from a vertex
  > * Transpose the Graph - Graph^T
  > * Using *DFS Algorithm* on Graph^T from the same vertex above.
  > * From both DFS's we receive a list that we do an Intersection between both lists
  > * The remaining elements are the SCC. 
* `plot_graph(self)` plots the graph. If the nodes have a position, the nodes will be placed there. Otherwise, they will be placed in a random but elegant manner. For this method we used matplotlib. Complexity - O(V+E)

![alt text](https://i.ibb.co/Sw5gYsL/Grrr.png)