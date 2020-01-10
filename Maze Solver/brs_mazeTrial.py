import time


class Maze():
    """A pathfinding problem."""

    def __init__(self, grid, location, path=[]):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
        self.path = path

    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print('O', end=' ')
                else:
                    print(self.grid[r][c], end=' ')
            print()
        print()

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        location = self.location
        row = location[0]
        col = location[1]
        posmoves = []

        #Add possible direction to possible moves list
        if self.grid[row][col + 1] != "X":  # East
            posmoves.append("E")
        if self.grid[row + 1][col] != "X":  # South
            posmoves.append("S")
        if self.grid[row - 1][col] != "X":  # North
            posmoves.append("N")
        if self.grid[row][col - 1] != "X":  # West
            posmoves.append("W")

        return posmoves

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        loc = self.location
        npath = self.path + [move]

        row = loc[0]
        col = loc[1]
        next_move = []
        if move == "E":
            next_move.append(row)
            next_move.append(col + 1)
        if move == "S":
            next_move.append(row + 1)
            next_move.append(col)
        if move == "W":
            next_move.append(row)
            next_move.append(col - 1)
        if move == "N":
            next_move.append(row - 1)
            next_move.append(col)

        return Maze(self.grid, tuple(next_move), npath)



class Agent():
    """Knows how to find the exit to a maze with BFS."""

    def bfsi(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        fringe = []
        fringe.append(maze)
        explored = [(1, 1)]
        # child = node.neighbor(move)
        while fringe:
            node = fringe.pop(0)
            for move in node.moves():
                if node.neighbor(move).location not in explored:
                    explored.append(node.neighbor(move).location)
                    node.neighbor(move).display()
                    if node.neighbor(move).location == goal.location:
                        return node.neighbor(move).path
                    fringe.append(node.neighbor(move))

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        fringe = []
        fringe.append(maze)
        explored = [(1, 1)]

        while fringe:
            node = fringe.pop(0)
            for move in node.moves():
                observer = node.neighbor(move)
                if observer.location not in explored:
                    explored.append(observer.location)
                    observer.display()
                    if observer.location == goal.location:
                        return observer.path
                    fringe.append(observer)




def main():
    """Create a maze, solve it with BFS, and console-animate."""
    grid = ["XXXXXXXXXXXXXXXXXXXX",
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

    grid2 = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
             'X         X                         X XX',
             'X XXXXX XXX XXX XXX XXXXXXXXXXX X XXX XX',
             'X     X       X   X           X X   X XX',
             'X X XXXXXXXXX XXXXX XXX XXX X XXXXXXX XX',
             'X X         X     X   X   X X       X XX',
             'X X XXX XXX X XXX XXXXXXXXXXXXXXX XXX XX',
             'X X   X   X X   X               X     XX',
             'X XXXXX X X X XXXXXXX X XXXXXXXXXXXXXXXX',
             'X     X X X X       X X               XX',
             'X XXXXX XXX XXXXXXXXX XXX X X XXXXX XXXX',
             'X     X X         X X   X X X     X   XX',
             'X XXXXX XXXXXXX X X XXXXX X X XXXXXXXXXX',
             'X     X       X X       X X X         XX',
             'X X XXXXXXX X XXXXX X XXX X X XXX XXXXXX',
             'X X       X X     X X   X X X X X     XX',
             'X XXX XXXXX XXX X X X XXXXXXXXX XXXXX XX',
             'X   X     X   X X X X               X XX',
             'X XXXXX XXX X X XXX X XXX X X X XXX X XX',
             'X     X   X X X   X X   X X X X   X X XX',
             'X X X X X X X XXXXXXX X XXX X X XXXXX XX',
             'X X X X X X X       X X   X X X     X XX',
             'X X X X XXXXXXXXX XXXXXXX X X XXXXXXXXXX',
             'X X X X         X       X X X         XX',
             'X X X X X XXX X X X XXXXXXXXX X X XXX XX',
             'X X X X X   X X X X         X X X   X XX',
             'X X X XXXXXXX XXX X XXXXX X XXXXX X X XX',
             'X X X       X   X X     X X     X X X XX',
             'X X X X XXXXX X XXX XXX XXX X X XXX XXXX',
             'X X X X     X X   X   X   X X X X     XX',
             'XXX XXX X X XXX XXX X XXX X X XXXXX X XX',
             'X     X X X   X   X X   X X X     X X XX',
             'X X X X X X X X X XXX XXXXX X XXXXX X XX',
             'X X X X X X X X X   X     X X     X X XX',
             'X X X XXX XXXXX X XXXXXXXXX XXXXX XXX XX',
             'X X X   X     X X       X       X   X XX',
             'X XXXXXXX XXXXXXX X X XXXXX XXXXXXX X XX',
             'X     X         X X X   X         X X XX',
             'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
             'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']

    grid3 = ['XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'X                             X       XX', 'X XXXXXXXXX X XXXXX XXXXXXX XXX XXX X XX', 'X         X X     X       X       X X XX', 'X X X X X X X X X XXXXX XXXXX X XXX XXXX', 'X X X X X X X X X     X     X X   X   XX', 'X X XXX X XXX XXX X X X XXXXX XXXXXXXXXX', 'X X   X X   X   X X X X     X   X     XX', 'X X X XXX XXXXX X X XXXXXXXXXXXXX XXX XX', 'X X X   X     X X X                 X XX', 'X X XXX X XXX X X X XXXXX XXXXXXXXX X XX', 'X X   X X   X X X X     X         X X XX', 'XXX X X X X X XXX X X X XXXXX XXXXX XXXX', 'X   X X X X X X   X X X     X     X   XX', 'X X X X X XXX X X X X XXXXXXX XXXXXXXXXX', 'X X X X X   X X X X X       X         XX', 'X X X X XXXXX XXX X X X X X X X XXX X XX', 'X X X X   X X   X X X X X X X X   X X XX', 'X X X X XXX XXX X X X X X X X X XXX XXXX', 'X X X X       X X X X X X X X X   X   XX', 'X X X X X X X XXXXX X XXXXXXX XXX X XXXX', 'X X X X X X X     X X       X   X X   XX', 'X X X X X XXX XXXXX X X X X X XXX XXX XX', 'X X X X X   X     X X X X X X   X   X XX', 'X XXX X X XXX XXXXX X XXXXXXX X XXXXXXXX', 'X X   X X   X     X X     X X X       XX', 'X X X X X X X XXXXXXX X XXX X X X X XXXX', 'X X X X X X X       X X     X X X X   XX', 'X XXX X X XXX X XXXXX XXXXXXXXX X X XXXX', 'X   X X X X   X     X         X X X   XX', 'X X XXXXX X X X X X X XXXXXXXXX X X XXXX', 'X X   X   X X X X X X       X X X X   XX', 'X X X XXX X X X X X X X X X X XXX XXXXXX', 'X X X   X X X X X X X X X X     X X   XX', 'X X XXX XXXXXXX X X X X XXXXXXX X X XXXX', 'X X   X X X X   X X X X       X X     XX', 'X X XXXXX X X X XXX X X XXXXXXXXXXXXX XX', 'X X         X X   X X X             X XX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']


    maze = Maze(grid3, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (37, 37))
    path = agent.bfs(maze, goal)
    solution = []
    count = 0

    while path:
        move = path.pop(0)
        solution.append(move)
        maze = maze.neighbor(move)
        time.sleep(0.3)
        maze.display()
        count = count + 1

    print("It took", count, "steps to complete the maze.")
    print("The path:")
    print(solution)
    print("\n\nNice")

if __name__ == '__main__':
    main()
