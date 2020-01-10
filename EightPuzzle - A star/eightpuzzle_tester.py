from eightpuzzle import *
import unittest

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.puzzle1_start = Puzzle([[1, 2, 5], [4, 8, 7], [3, 6, ' ']])
        self.puzzle1_goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    def test_moves(self):
        self.assertCountEqual(self.puzzle1_start.moves(), ["N","W"])
        self.assertCountEqual(self.puzzle1_goal.moves(), ["E", "S"])
    def test_neighbor(self):
        self.m2 = self.puzzle1_start.neighbor("N")
        self.assertEqual(self.m2.grid, [[1, 2, 5], [4, 8, ' '], [3, 6, 7]])
    def test_astar(self):
        self.assertEqual(Agent().astar(self.puzzle1_start,self.puzzle1_goal), ['N', 'W', 'W', 'S', 'E', 'E', 'N', 'N', 'W', 'W'])

if __name__ == '__main__':
    unittest.main(verbosity=2)