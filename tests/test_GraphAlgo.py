import unittest

from ex3.src.DiGraph import DiGraph
from ex3.src.GraphAlgo import GraphAlgo


class test_GraphAlgo(unittest.TestCase):

    def create_graph(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_node(7)
        g.add_node(8)
        g.add_node(9)

        g.add_edge(0, 1, 1)
        g.add_edge(1, 2, 2.1)
        g.add_edge(2, 0, 3)
        g.add_edge(2, 3, 5.5)
        g.add_edge(3, 2, 5.5)
        g.add_edge(3, 4, 4)
        g.add_edge(4, 5, 2)
        g.add_edge(5, 3, 3.4)
        g.add_edge(5, 6, 1)
        g.add_edge(6, 7, 5)
        g.add_edge(7, 8, 4.8)  # 4.8 fails  exp 37.4
        g.add_edge(8, 6, 1.9)
        g.add_edge(8, 9, 12)

        return g

    def test_save_and_load_json(self):
        graph = self.create_graph()
        g1_algo = GraphAlgo(graph)
        g1_algo.save_to_json("Test.json")
        g2_algo = GraphAlgo()
        g2_algo.load_from_json("Test.json")
        self.assertTrue(g1_algo.graph.__eq__(g2_algo.graph))
        self.assertEqual(g1_algo.graph.v_size(), g2_algo.graph.v_size())
        self.assertEqual(g1_algo.graph.e_size(), g2_algo.graph.e_size())
        g2_algo.graph.remove_node(3)
        self.assertNotEqual(g1_algo.graph.v_size(), g2_algo.graph.v_size())
        self.assertNotEqual(g1_algo.graph.e_size(), g2_algo.graph.e_size())

    def test_shortest_path(self):
        graph = self.create_graph()
        g_algo = GraphAlgo(graph)
        x = (37.4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        # self.assertEquals(x, g_algo.shortest_path(0, 9), 0.1)
        graph.add_edge(0, 3, 2)
        self.assertNotEqual(x, g_algo.shortest_path(0, 9))
        graph.add_edge(0, 2, 3.5)
        x = (3.1, [0, 1, 2])
        self.assertEqual(x, g_algo.shortest_path(0, 2))
        x = (float('infinity'), [])
        self.assertEqual(x, g_algo.shortest_path(20, 0))
        self.assertEqual(x, g_algo.shortest_path(6, 5))
        graph.remove_node(3)
        self.assertEqual(x, g_algo.shortest_path(0, 9))
        graph.remove_edge(5, 6)
        self.assertEqual(x, g_algo.shortest_path(4, 9))
        x = (0, [0])
        self.assertEqual(x, g_algo.shortest_path(0, 0))

    def test_connected_component(self):
        graph = self.create_graph()
        g_algo = GraphAlgo(None)
        x = []
        self.assertEqual(x, g_algo.connected_components())
        g_algo = GraphAlgo(graph)
        x = []
        self.assertEqual(x, g_algo.connected_component(20))
        x = [0, 1, 2, 3, 4, 5]
        self.assertEqual(x, g_algo.connected_component(0))
        graph.remove_edge(3, 2)
        x = [0, 1, 2]
        self.assertEqual(x, g_algo.connected_component(0))
        graph.add_edge(3, 2, 1)
        graph.add_edge(6, 5, 7)
        graph.add_edge(9, 8, 2)
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(x, g_algo.connected_component(5))

    def test_connected_components(self):
        graph = self.create_graph()
        g_algo = GraphAlgo(None)
        x = []
        self.assertEqual(x, g_algo.connected_components())
        g_algo = GraphAlgo(graph)
        x = [[0, 1, 2, 3, 4, 5], [8, 6, 7], [9]]
        self.assertEqual(x, g_algo.connected_components())
        graph.remove_edge(2, 3)
        graph.add_edge(9, 8, 10)
        x = [[0, 1, 2], [3, 4, 5], [8, 9, 6, 7]]
        self.assertEqual(x, g_algo.connected_components())

    if __name__ == '__main__':
        unittest.main()
