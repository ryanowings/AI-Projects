import time
#Ryan Owings
#CSC 481 AI 9/24/2019
#HW1 Maze Solver 5000


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

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        fringe = []
        fringe.append(maze)
        explored = [(1, 1)]  # starting location (1,1) explored

        while fringe:
            node = fringe.pop(0)  # Look at first maze instance and remove from fringe
            for move in node.moves():  # all possible moves
                observer = node.neighbor(move)  # observer = child after move
                if observer.location not in explored:  # if the observer is a new location
                    explored.append(observer.location)  # its now explored
                    if observer.location == goal.location:  # if we are at the end
                        return observer.path  # return the path to get there, solution
                    fringe.append(observer)  # end not found, add  the next step to the fringe


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

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
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
