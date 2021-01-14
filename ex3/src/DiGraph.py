from ex3.src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):
        self.modeCount = 0
        self.v_Size = 0
        self.e_Size = 0
        self.Nodes = {}  # All Vertices
        self.EdgesSrc = {}  # All From Src
        self.EdgesDst = {}  # All to Src from Dst
        self.pos = {}

    def v_size(self) -> int:
        return self.v_Size

    def e_size(self) -> int:
        return self.e_Size

    def get_mc(self) -> int:
        return self.modeCount

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        src = id1
        dst = id2

        if src == dst or weight < 0:
            return False

        src_e = EdgeData(src, dst, weight)
        dest_e = EdgeData(dst, src, weight)

        if src in self.Nodes.keys() and dst in self.Nodes.keys():
            if src in self.EdgesDst[dst] and dst in self.EdgesSrc[src]:
                return False
            else:
                self.EdgesSrc[src][dst] = src_e
                self.EdgesDst[dst][src] = dest_e
                self.e_Size += 1
                self.modeCount += 1

                return True

        return False


def add_node(self, node_id: int, pos: tuple = None) -> bool:
    if node_id in self.Nodes.keys():
        return False

    self.Nodes[node_id] = NodeData(node_id, pos=pos)  # NeedFix
    self.EdgesSrc[node_id] = {}
    self.EdgesDst[node_id] = {}

    self.v_Size += 1
    self.modeCount += 1
    return True


def remove_node(self, node_id: int) -> bool:
    if node_id not in self.Nodes.keys():
        return False

    for edge in self.EdgesDst.get(node_id).keys():
        self.EdgesSrc.get(edge).pop(node_id)
        self.e_Size -= 1

    for edge in self.EdgesSrc.get(node_id).keys():
        self.EdgesDst.get(edge).pop(node_id)
        self.e_Size -= 1

    self.EdgesSrc.pop(node_id)
    self.Nodes.pop(node_id)
    self.EdgesDst.pop(node_id)
    self.v_Size -= 1
    self.modeCount += 1
    return True


def remove_edge(self, node_id1: int, node_id2: int) -> bool:
    if node_id1 in self.Nodes.keys() and node_id2 in self.Nodes.keys():
        if node_id1 in self.EdgesDst[node_id2] and node_id2 in self.EdgesSrc[node_id1]:
            self.EdgesSrc[node_id1].pop(node_id2)
            self.EdgesDst[node_id2].pop(node_id1)
            self.e_Size -= 1
            self.modeCount += 1
        else:
            return False
    return False


def get_all_v(self) -> dict:
    return self.Nodes.values()


def all_in_edges_of_node(self, id1: int) -> dict:
    if id1 not in self.Nodes.keys():
        return

    return self.EdgesDst[id1]


def all_out_edges_of_node(self, id1: int) -> dict:
    if id1 not in self.Nodes.keys():
        return

    return self.EdgesSrc[id1]


def __str__(self):
    string = "\n"
    for vertex in self.Nodes.values():
        string += f"Key: {vertex} \n"
        string += "Edges To:  \n["
        for edge in self.EdgesSrc[vertex.key].values():
            string += f"{vertex.key} -> ({edge.dst}) W: ~{edge.weight}~, "
        string += "]\nEdges From: \n["
        for edge in self.EdgesDst[vertex.key].values():
            string += f"{vertex.key} <- ({edge.dst}), "
        string += "]\n"

    return string


def __repr__(self):
    string = "\n"
    for vertex in self.Nodes.values():
        string += f"Key: {vertex} \n"
        string += "Edges To:  \n["
        for edge in self.EdgesSrc[vertex.key].values():
            string += f"{vertex.key} -> ({edge.dst}) W: ~{edge.weight}~, "
        string += "]\nEdges From: \n["
        for edge in self.EdgesDst[vertex.key].values():
            string += f"{vertex.key} <- ({edge.dst}), "
        string += "]\n"

    return string


class Point3D:
    """
    An Object to Contain a Position in R^3 space
    """
    def __init__(self, pos: tuple = (0, 0, 0)):
        self.pos = pos

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self):
        return f"pos: x={self.pos[0]} y={self.pos[1]} z={self.pos[2]}"

    def __repr__(self):
        return f"pos: x={self.pos[0]} y={self.pos[1]} z={self.pos[2]}"


class NodeData:
    """
    An Object to Contain the vertices in a Graph (Key,Position)
    """
    def __init__(self, key, pos: Point3D = None):
        self.pos = pos
        self.key = key
        self.tag = -1
        self.r_from = ""

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self):
        return f"Key: {self.key} pos: {self.pos}"

    def __repr__(self):
        return f"Key: {self.key} pos: {self.pos}"


class EdgeData:
    """
    An Object to Contain the edges in a Graph  src->dst(w)
    """
    def __init__(self, src: int, dst: int, weight):
        self.src = src
        self.dst = dst
        self.weight = weight

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __str__(self):
        return f"[Src :{self.src} -> Dst : {self.dst} Weight : {self.weight}]"

    def __repr__(self):
        return f"[Src :{self.src} -> Dst : {self.dst} Weight : {self.weight}]"
