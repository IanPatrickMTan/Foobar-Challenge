def branch(maze, tips, covered, covBreakers, breakers):
    dim = [len(maze), len(maze[0])]
    newTips = []
    newBreakers = []
    for tip, breaker in zip(tips, breakers):
        neighbors = [[tip[0] + 1, tip[1]], [tip[0] - 1, tip[1]], [tip[0], tip[1] + 1], [tip[0], tip[1] - 1]]
        for neighbor in neighbors:
            if neighbor in covered:
                if not covBreakers[covered.index(neighbor)] and breaker:
                    if -1 < neighbor[0] < dim[0] and -1 < neighbor[1] < dim[1]:
                        if maze[neighbor[0]][neighbor[1]]:
                            if breaker and not neighbor in newTips:
                                newTips.append(neighbor)
                                newBreakers.append(False)
                        else:
                            if neighbor in newTips:
                                if not newBreakers[newTips.index(neighbor)] and breaker:
                                    newBreakers[newTips.index(neighbor)] = True
                            else:
                                newTips.append(neighbor)
                                newBreakers.append(breaker)

            else:
                if -1 < neighbor[0] < dim[0] and -1 < neighbor[1] < dim[1]:
                    if maze[neighbor[0]][neighbor[1]]:
                        if breaker and not neighbor in newTips:
                            newTips.append(neighbor)
                            newBreakers.append(False)
                    else:
                        if neighbor in newTips:
                            if not newBreakers[newTips.index(neighbor)] and breaker:
                                newBreakers[newTips.index(neighbor)] = True
                        else:
                            newTips.append(neighbor)
                            newBreakers.append(breaker)
    return newTips, covered + newTips, covBreakers + newBreakers, newBreakers

def solution(maze):
    dim = [len(maze), len(maze[0])]
    tips = [[0, 0]]
    covered = [[0, 0]]
    covBreakers = [True]
    breakers = [True]
    x = 1
    while not [dim[0] - 1, dim[1] - 1] in tips:
        x += 1
        tips, covered, breakers = branch(maze, tips, covered, covBreakers, breakers)    
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
