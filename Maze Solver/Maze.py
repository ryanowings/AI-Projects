# author: John Rowan
# class: CSC 481-80 TR 5:45 - 7:00
# professor: Dr. Richard Burns
# project: bfs_maze -- Maze.py
# created: 9/6/2019 10:11 PM
# Maze.py
# Last update 20031115-214011

"""
implements class Maze

Three public methods are implemented:
  __init__(rows,cols)
  __str__()
  as_html_table()

Usage:
  maze = Maze( 20, 30 )  # create a maze 20 rows x 30 cols
  print maze             # print out the maze
  print "<html><body>%s</body></html>" % maze.as_html_table() # publish it

To do:
  1. Method find_path() :)
  2. Different algorithms for big mazes (>50x50) or iteration instead of recursion
"""

from __future__ import print_function



import random

import sys




EMPTY = ' '

WALL = 'X'

AGENT = ' '

GOAL = ' '



def adjacent(cell):

  i,j = cell

  for (y,x) in ((1,0), (0,1), (-1, 0), (0,-1)):

    yield (i+y, j+x), (i+2*y, j+2*x)



def generate(width, height, verbose=True):

  '''Generates a maze as a list of strings.



     :param width: the width of the maze, not including border walls.

     :param heihgt: height of the maze, not including border walls.

  '''

  # add 2 for border walls.

  global agentlocation
  global goallocation
  #width += 2

  #height += 2

  rows, cols = height, width



  maze = {}



  spaceCells = set()

  connected = set()

  walls = set()



  # Initialize with grid.

  for i in range(rows):

    for j in range(cols):

      if (i%2 == 1) and (j%2 == 1):

        maze[(i,j)] = EMPTY

      else:

        maze[(i,j)] = WALL



  # Fill in border.

  for i in range(rows):

    maze[(i,0)] = WALL

    maze[(i,cols-1)] = WALL

  for j in range(cols):

    maze[(0,j)] = WALL

    maze[(rows-1,j)] = WALL



  for i in range(rows):

    for j in range(cols):

      if maze[(i,j)] == EMPTY:

        spaceCells.add((i,j))

      if maze[(i,j)] == WALL:

        walls.add((i,j))



  # Prim's algorithm to knock down walls.

  originalSize = len(spaceCells)

  connected.add((1,1))

  while len(connected) < len(spaceCells):

    doA, doB = None, None

    cns = list(connected)

    random.shuffle(cns)

    for (i,j) in cns:

      if doA is not None: break

      for A, B in adjacent((i,j)):

        if A not in walls:

          continue

        if (B not in spaceCells) or (B in connected):

          continue

        doA, doB = A, B

        break

    A, B = doA, doB

    maze[A] = EMPTY

    walls.remove(A)

    spaceCells.add(A)

    connected.add(A)

    connected.add(B)

    if verbose:

      cs, ss = len(connected), len(spaceCells)

      cs += (originalSize - ss)

      ss += (originalSize - ss)





  # Insert character and goals.

  TL = (1,1)

  BR = (rows-2, cols-2)

  if rows % 2 == 0:

    BR = (BR[0]-1, BR[1])

  if cols % 2 == 0:

    BR = (BR[0], BR[1]-1)



  maze[TL] = AGENT
  agentlocation = list(TL)

  maze[BR] = GOAL
  goallocation = list(BR)



  lines = []

  for i in range(rows):

    lines.append(''.join(maze[(i,j)] for j in range(cols)))



  return lines

def main():

    width = 40

    height = 40

    maze = generate(width, height)

    #print('\n'.join(maze))
    print(maze)
    print('\n')
    print("agent Location: ")
    print(agentlocation)
    print("goal location")
    print(goallocation)

if __name__ == '__main__':
  main()
