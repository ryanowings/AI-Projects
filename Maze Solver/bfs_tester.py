from bfs_maze import *
import unittest


class Grids():

    def __init__(self):
        self.grid1 = ["XXXXXXXXXXXXXXXXXXXX",
                      "X     X    X       X",
                      "X XXXXX XXXX XXX XXX",
                      "X       X      X X X",
                      "X X XXX XXXXXX X X X",
                      "X X   X        X X X",
                      "X XXX XXXXXX XXXXX X",
                      "X XXX    X X X     X",
                      "X    XXX       XXXXX",
                      "XXXXX   XXXXXX     X",
                      "X   XXX X X    X X X",
                      "XXX XXX X X XXXX X X",
                      "X     X X   XX X X X",
                      "XXXXX     XXXX X XXX",
                      "X     X XXX    X   X",
                      "X XXXXX X XXXX XXX X",
                      "X X     X  X X     X",
                      "X X XXXXXX X XXXXX X",
                      "X X                X",
                      "XXXXXXXXXXXXXXXXXX X"]


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.m1 = Maze(Grids().grid1, (1, 1))
        self.g1 = Maze(Grids().grid1, (19, 18))

    def test_moves(self):
        self.assertCountEqual(self.m1.moves(), ["E", "S"])

    def test_neighbor(self):
        self.m2 = self.m1.neighbor("S")
        self.assertEqual(self.m1.grid, self.m2.grid)
        self.assertEqual(self.m2.location, (2, 1))

    def test_bfs(self):
        self.assertEqual(Agent().bfs(self.m1, self.g1),
                         ['S', 'S', 'E', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'S',
                          'E', 'E', 'S', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'S', 'S'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
