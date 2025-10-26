# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List
from util import Stack, Queue, PriorityQueue, hashTable
from util import manhattanDistance as mnhtn

dict = {
        "North": Directions.NORTH,
        "South": Directions.SOUTH,
        "West": Directions.WEST,
        "East": Directions.EAST,
    }

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def actionSeries(state0:tuple,state1:tuple)-> list:
    # state0:start & state1:end node
    action = Stack()
    state = state1
    while state!=state0:
        action.push(table.get(state)[1])
        state = table.get(state)[0]
    actions = []
    while action.isEmpty()!=True:
        actions.append(action.pop())
    return actions

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    
    global table
    table = hashTable()
    fringe=Stack()
    state0 = problem.getStartState()
    print(f"start state is:",state0)
    state=state0
    table.insert(state,'','')

    while True:
        parent=state
        for i in problem.getSuccessors(state):
            fringe.push(i)
        alt = fringe.pop()
        x=0
        while table.lookup(alt[0])==True and fringe.isEmpty()!=True:
            alt = fringe.pop()
            x+=1
        state = alt[0]

        # Finding parent in backtrack
        if x!=0:
            for i in problem.getSuccessors(alt[0]):
                if table.lookup(i[0])==True: parent = i[0]
        table.insert(alt[0],(parent[0],parent[1]),dict.get(alt[1]))
        if problem.isGoalState(state)==True:
            break
    return actionSeries(state0,state)
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    
    global table
    table=hashTable()
    fringe=Queue()
    state0 = problem.getStartState()
    print(f"start state is:",state0)
    state=state0
    table.insert(state,'','')

    while True:
        for i in problem.getSuccessors(state):
            fringe.push(i)
        alt = fringe.pop()
        while table.lookup(alt[0])==True and fringe.isEmpty()!=True:
            alt = fringe.pop()
        state = alt[0]
        for i in problem.getSuccessors(state):
            if table.lookup(i[0])==True: parent = i[0]
        table.insert(alt[0],(parent[0],parent[1]),dict.get(alt[1]))
        if problem.isGoalState(state)==True:
            break

    return actionSeries(state0,state)
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    global table
    table=hashTable()
    fringe=PriorityQueue()
    
    state0 = problem.getStartState()
    print(f"start state is:",state0)
    state=state0
    table.insert(state,'','')

    while True:
        for i in problem.getSuccessors(state):
            if table.lookup(i[0])==False:
                table.insert(i[0],(state[0],state[1]),dict.get(i[1]))
                if i[0]!=state0: 
                    fringe.push(i,problem.getCostOfActions(actionSeries(state0,i[0])))
        alt = fringe.pop()
        state = alt[0]
        if problem.isGoalState(state)==True:
            break
    return actionSeries(state0,state)
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    global table
    table=hashTable()
    fringe=PriorityQueue()
    
    state0 = problem.getStartState()
    xy0=[state0[0],state0[1]]
    print(f"start state is:",state0)
    state=state0
    table.insert(state,'','')

    while True:
        for i in problem.getSuccessors(state):
            if table.lookup(i[0])==False:
                table.insert(i[0],(state[0],state[1]),dict.get(i[1]))
                if i[0]!=state0:
                    xy1=[i[0][0],i[0][1]]
                    fringe.push(i,(problem.getCostOfActions(actionSeries(state0,i[0]))+mnhtn(xy0,xy1)))
        alt = fringe.pop()
        state = alt[0]
        if problem.isGoalState(state)==True:
            break
    return actionSeries(state0,state)
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
