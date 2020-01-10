# Ryan Owings
# 8 puzzle using a*
# 10/1/2019
# CSC 481 R. Burns AI

import copy
import time

class Puzzle():
    """A sliding-block puzzle."""

    def __init__(self, grid, path=[]):
        """Instances differ by their number configurations."""
        self.grid = copy.deepcopy(grid)  # No aliasing!
        self.path = path

    def display(self):
        """Print the puzzle."""
        for row in self.grid:
            for number in row:
                print(number, end=' ')
                # print number,
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current configuration."""
        rloc = 0
        cloc = 0
        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == ' ':
                    loc = self.grid[r][c]
                    rloc = r
                    cloc = c


        posmoves = []
        if (rloc - 1) >= 0:
            posmoves.append("N")
        if (cloc - 1) >= 0:
            posmoves.append("W")
        if (rloc + 1) < 3:
            posmoves.append("S")

        if (cloc + 1) < 3:
            posmoves.append("E")

        return posmoves

    def neighbor(self, move):
        """Return a Puzzle instance like this one but with one move made."""

        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == ' ':
                    loc = self.grid[r][c]
                    rloc = r
                    cloc = c
        if move == "N":
            npath = self.path + [move]
            updated = copy.deepcopy(self.grid)
            updated[rloc][cloc] = updated[rloc - 1][cloc]
            updated[rloc - 1][cloc] = ' '
        if move == "S":
            npath = self.path + [move]
            updated = copy.deepcopy(self.grid)
            updated[rloc][cloc] = updated[rloc + 1][cloc]
            updated[rloc + 1][cloc] = ' '
        if move == "W":
            npath = self.path + [move]
            updated = copy.deepcopy(self.grid)
            updated[rloc][cloc] = updated[rloc][cloc - 1]
            updated[rloc][cloc - 1] = ' '
        if move == "E":
            npath = self.path + [move]
            updated = copy.deepcopy(self.grid)
            updated[rloc][cloc] = updated[rloc][cloc + 1]
            updated[rloc][cloc + 1] = ' '
        return Puzzle(updated, npath)


    def h(self, goal):
        manD = 0
        for i in range(3):
            for j in range(3):
                if goal.grid[i][j] != ' ':
                    goalloc = goal.grid[i][j]

                    goali = i
                    goalj = j

                    loci = 0
                    locj = 0

                    for x in range(3):
                        for y in range(3):
                            loc = self.grid[x][y]
                            if loc == goalloc:
                                locj = y
                                loci = x

                    manD += abs(goali - loci) + abs(goalj - locj)

        return manD


class pq(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == []

    def insert(self, puzzle, h):
        self.queue.append((puzzle, h))

    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] < self.queue[min][1]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()


class Agent():
    """Knows how to solve a sliding-block puzzle with A* search."""

    def astar(self, puzzle, goal):
        """Return a list of moves to get the puzzle to match the goal."""
        finished = []
        fringe = pq()

        fringe.insert(puzzle, puzzle.h(goal))

        while fringe:
            min = fringe.delete()

            if min[0].grid == goal.grid:
                return min[0].path

            finished.append(min[0].grid)
            par = min[0].moves()

            for move in par:
                child = min[0].neighbor(move)

                if child.grid in finished:
                    continue
                else:
                    finished.append(child.grid)
                    print(child.grid)
                    fringe.insert(child, child.h(goal))


def main():
    """Create a puzzle, solve it with A*, and console-animate."""

    puzzle = Puzzle([[8, 7, 6], [4, 5, 3], [1, 2, ' ']])
    puzzle1 = Puzzle([[5, ' ', 8], [4, 2, 1], [7, 3, 6]])
    puzzle.display()

    agent = Agent()
    goal = Puzzle([[' ', 1, 2], [3, 4, 5], [6, 7, 8]])
    goal1 = Puzzle([[1, 2, 3], [4, 5, 6], [7, 8, ' ']])
    path = agent.astar(puzzle1, goal1)
    print(path)
    while path:
        move = path.pop(0)
        puzzle = puzzle.neighbor(move)
        time.sleep(1)
        puzzle.display()


if __name__ == '__main__':
    main()
