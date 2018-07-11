"""

Maze building file
description: class to generate a maze for the player
 Directions: 1 = up, 2 = right, 3 = down, 4 = left

"""

from random import randint, shuffle
from enum import Enum

Direction = {}
Direction['LEFT'] = 4
Direction['RIGHT'] = 2
Direction['UP'] = 1
Direction['DOWN'] = 3

class Node(object):
  """"""
  def __init__(self, x, y, directions, current, prevNodeLocation=-1):
    self.x = x
    self.y = y
    self.directions = directions

    # shuffle direction for different maze build
    shuffle(self.directions)
    self.current = current

    if prevNodeLocation == -1:
      self.prevNodeLocation = self.directions[0]
    else:
      self.prevNodeLocation = prevNodeLocation

class Mazebuilder():
  """docstring for Mazebuilder"""
  def __init__(self, size):
    self.size = size
    self.maze = [[] for _ in range(0, size)]
    for i in range(0, size):
      for j in range(0, size):
        self.maze[i].append(0)

  def setMazeValue(self, x, y, value):
    self.maze[x][y] = value
    return

  def getMazeValue(self, x, y):
    return self.maze[x][y]

  def printoutMaze(self):
    # for i in range(0,self.size):
    #   t = []
    #   for j in range(0, self.size):
    #     t.append(self.getMazeValue(i, j)) 
    #   print(t)
    print(self.maze)
    return

  def checkNewNode(self, newX, newY, prevNodeLocation):
    for neighborNode in range(1, 5):
      if((newY <=0) or (newY + 1 >= self.size) 
        or (newX <=0) or (newX + 1 >= self.size)):
        return False

      """
      To understand what is happening here:
      1. First it checks previous neighbor P if corners X are not equal to 1 
      i.e for 1,
      0  0  0
      0  N  0
      X  P  X
      2. if not check neighbors if any > 1
      0  X  0
      X  N  X
      0  P  0
      """

      if(neighborNode == Direction['UP']):
        if(neighborNode == prevNodeLocation): 
          if((self.getMazeValue((newX - 1), (newY + 1)) > 0) or 
            (self.getMazeValue((newX + 1), (newY + 1)) > 0)):
            return False

        elif(self.getMazeValue(newX, newY - 1) > 0):
          return False

      elif(neighborNode == Direction['RIGHT']):
        if(neighborNode == prevNodeLocation):
          if((self.getMazeValue((newX - 1), (newY - 1)) > 0) or 
            (self.getMazeValue((newX - 1), (newY + 1)) > 0)):
            return False

        elif(self.getMazeValue(newX + 1, newY) > 0):
          return False

      elif(neighborNode == Direction['DOWN']):
        if(neighborNode == prevNodeLocation): 
          if ((self.getMazeValue((newX - 1), (newY - 1)) > 0) or 
            (self.getMazeValue((newX + 1), (newY - 1)) > 0)):
            return False

        elif(self.getMazeValue(newX, newY + 1) > 0):
          return False

      elif(neighborNode == Direction['LEFT']):
        if(neighborNode == prevNodeLocation): 
          if ((self.getMazeValue((newX + 1), (newY - 1)) > 0) or 
            (self.getMazeValue((newX + 1), (newY + 1)) > 0)):
            return False

        elif(self.getMazeValue(newX - 1, newY) > 0):
          return False
    return True

  def createMaze(self):
    directions = [Direction['LEFT'], Direction['RIGHT'], Direction['UP'], Direction['DOWN']]
    nodeStack = []

    # starting location
    currentX, currentY = 1, 1
    self.setMazeValue(currentX, currentY, 1)

    # create new node and add to stack
    currentNode = Node(currentX, currentY, directions[:], 0)
    nodeStack.append(currentNode)

    # create maze until stack is empty
    while (nodeStack):
      newNodeX, newNodeY = 0, 0
      newNodeCurrent, previousNodePosition = 0, 0
      currentNode = nodeStack.pop()
      self.setMazeValue(currentNode.x, currentNode.y, 1)

      # move to next direction in current node's direction list
      currentDirection = currentNode.directions[currentNode.current]

      if(currentDirection == Direction['UP']):
        newNodeX, newNodeY = currentNode.x, currentNode.y - 1
        previousNodePosition = Direction['DOWN']
      elif(currentDirection == Direction['RIGHT']):
        newNodeX, newNodeY = currentNode.x + 1, currentNode.y
        previousNodePosition = Direction['LEFT']
      elif(currentDirection == Direction['DOWN']):
        newNodeX, newNodeY = currentNode.x, currentNode.y + 1
        previousNodePosition = Direction['UP']
      elif(currentDirection == Direction['LEFT']):
        newNodeX, newNodeY = currentNode.x - 1, currentNode.y
        previousNodePosition = Direction['RIGHT']
      else:
        return "should not get here"
      
      # update current direction
      currentNode.current+=1

      # check if node has went through all directions
      if currentNode.current < 4:
        nodeStack.append(currentNode)

      # do check if node is valid to move to
      check = self.checkNewNode(newNodeX, newNodeY, previousNodePosition)
      if check:
        newNode = Node(newNodeX, newNodeY, directions[:], 0, previousNodePosition)
        nodeStack.append(newNode)

    # Set start (2) and end (3) location
    self.setMazeValue(1, 1, 2)
    endLocationX, endLocationY = self.size - 1, self.size - 1
    while(self.getMazeValue(endLocationX, endLocationY) == 0):
      if(endLocationX < endLocationY):
        endLocationY-=1
      else:
        endLocationX-=1
    self.setMazeValue(endLocationX, endLocationY, 3)
    # # print out maze for verification (TESTING)
    # self.printoutMaze()
    return













