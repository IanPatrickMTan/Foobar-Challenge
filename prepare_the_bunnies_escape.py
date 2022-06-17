"""
Prepare the Bunnies' Escape
===========================

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny workers, but once they're free of the work duties the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a work area exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the station is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the station door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.
"""

import numpy as np

def display(maze):
    for x in maze:
        for y in x:
            print('█' if y else '▢', end='')
        print()

def walkable(maze):
    maze = np.array(maze)
    openPlaces = np.where(maze == 0)
    return openPlaces

def hollow(maze):
    maze = np.array(maze)
    openPlaces = walkable(maze[:-2, :-2])
    hollowWalls = walkable(maze[:])

def branch(maze, tips, covered, breakers):
    dim = [len(maze), len(maze[0])]
    newTips = []
    newBreakers = []
    for tip, breaker in zip(tips, breakers):
        print(f'\ntip: {tip}\nable to break: {breaker}\n')
        neighbors = [[tip[0] + 1, tip[1]], [tip[0] - 1, tip[1]], [tip[0], tip[1] + 1], [tip[0], tip[1] - 1]]
        for neighbor in neighbors:
            print(f'neighbor: {neighbor}')
            if not neighbor in tips and -1 < neighbor[0] < dim[0] and -1 < neighbor[1] < dim[1]:
                print('neighbor is valid')
                if maze[neighbor[0]][neighbor[1]]:
                    print('neighbor is wall')
                    if breaker and not neighbor in newTips:
                        print('breakable')
                        newTips.append(neighbor)
                        newBreakers.append(False)
                else:
                    print('neighbor is empty')
                    if neighbor in newTips:
                        if not newBreakers[newTips.index(neighbor)] and breaker:
                            print('ALERT: REROUTED')
                            newBreakers[newTips.index(neighbor)] = True
                    else:
                        newTips.append(neighbor)
                        newBreakers.append(breaker)
            else:
                print('neighbor is invalid because ' + 'it was covered' if neighbor in covered else 'because it was out of range')
    return newTips, covered + newTips, newBreakers

def solution(maze):
    dim = [len(maze), len(maze[0])]
    tips = [[0, 0]]
    covered = [[0, 0]]
    breakers = [True]
    x = 1
    while not [dim[0] - 1, dim[1] - 1] in tips:
        print(f'\n\n\titeration: {x}\n\n')
        x += 1
        tips, covered, breakers = branch(maze, tips, covered, breakers)    
        print(tips, covered, breakers)
    return x


        
tips = [[0, 0]]
covered = [[0, 0]]
breakers = [True]

ft, fc, fb = [[2, 0], [1, 1]], [[0, 0], [1, 0], [0, 1], [2, 0], [1, 1]], [False, True]

maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
maze1 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
mazex = [
   [0, 1, 0, 1, 0, 0, 0], 
   [0, 0, 0, 1, 0, 1, 0]
]
koral = [[0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0]]
