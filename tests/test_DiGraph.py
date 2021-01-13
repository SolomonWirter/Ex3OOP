import unittest

from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_add_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(graph.v_size(), 10)
        graph.add_node(21)
        self.assertEqual(graph.v_size(), 11)
        graph.add_node(-10)
        self.assertEqual(graph.v_size(), 12)
        graph.add_node(7)
        self.assertEqual(graph.v_size(), 12)

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i+1, i*2 + 1)
        self.assertEqual(graph.e_size(), 9)
        graph.add_edge(9, 0, 5.5)
        self.assertEqual(graph.e_size(), 10)
        graph.add_edge(1, 3, 2.7)
        graph.add_edge(9, 4, 3)
        self.assertEqual(graph.e_size(), 12)
        graph.add_edge(9, 4, 3)
        self.assertEqual(graph.e_size(), 12)
        graph.add_edge(2, 2, 100)
        self.assertEqual(graph.e_size(), 12)
        graph.add_edge(6, 7, -3)
        self.assertEqual(graph.e_size(), 12)
        graph.add_edge(15, 8, 100)
        self.assertEqual(graph.e_size(), 12)
        graph.add_edge(0, 1, 10)
        self.assertEqual(graph.e_size(), 12)

    def test_remove_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        self.assertTrue(graph.remove_node(0))
        self.assertEqual(graph.e_size(), 8)
        self.assertEqual(graph.v_size(), 9)
        self.assertFalse(0 in graph.Nodes.keys())
        self.assertTrue(8 in graph.Nodes.keys())
        self.assertFalse(graph.remove_node(0))
        self.assertFalse(graph.remove_node(20))
        self.assertEqual(graph.v_size(), 9)

    def test_remove_edge(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        graph.remove_edge(2, 3)
        self.assertEqual(graph.v_size(), 10)
        self.assertEqual(graph.e_size(), 8)
        self.assertFalse(graph.all_out_edges_of_node(2).__contains__(3))
        self.assertFalse(graph.all_in_edges_of_node(3).__contains__(2))
        self.assertFalse(graph.remove_edge(6, 0))
        self.assertFalse(graph.remove_edge(5, 100))

    def test_get_all_v(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        l = []
        for vertex in graph.Nodes.values():
            l.append(vertex)
        for vertex in l:
            self.assertIn(vertex, graph.get_all_v())
        graph.remove_node(3)
        self.assertNotIn(3, graph.get_all_v())

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        self.assertTrue(graph.all_in_edges_of_node(1).__contains__(0))
        graph.remove_edge(0, 1)
        self.assertFalse(graph.all_in_edges_of_node(1).__contains__(0))
        graph.add_node(12)
        graph.add_edge(12, 4, 19)
        self.assertIn(12, graph.all_in_edges_of_node(4))

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        self.assertTrue(graph.all_out_edges_of_node(0).__contains__(1))
        graph.remove_edge(0, 1)
        self.assertFalse(graph.all_in_edges_of_node(0).__contains__(1))
        graph.add_node(12)
        graph.add_edge(12, 4, 19)
        self.assertIn(4, graph.all_out_edges_of_node(12))

    def test_get_mc(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, i * 2 + 1)
        self.assertEqual(graph.get_mc(), 19)
        graph.remove_edge(0, 1)
        self.assertEqual(graph.get_mc(), 20)
        graph.add_edge(0, 1, 1)
        self.assertEqual(graph.get_mc(), 21)
        graph.add_edge(0, 1, 1)
        self.assertEqual(graph.get_mc(), 21)
        graph.remove_node(0)
        self.assertEqual(graph.get_mc(), 22)
        graph.remove_node(0)
        self.assertEqual(graph.get_mc(), 22)
        graph.add_node(0)
        self.assertEqual(graph.get_mc(), 23)
        graph.add_node(0)
        self.assertEqual(graph.get_mc(), 23)

    if __name__ == '__main__':
        unittest.main()
