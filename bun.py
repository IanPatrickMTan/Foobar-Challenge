def branch(maze, tips, covered, breakers):
    dim = [len(maze), len(maze[0])]
    newTips = []
    newBreakers = []
    for tip, breaker in zip(tips, breakers):
        neighbors = [[tip[0] + 1, tip[1]], [tip[0] - 1, tip[1]], [tip[0], tip[1] + 1], [tip[0], tip[1] - 1]]
        for neighbor in neighbors:
            
            if not neighbor in covered and -1 < neighbor[0] < dim[0] and -1 < neighbor[1] < dim[1]:
                
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
                        newBreakers.append(True)
    return newTips, covered + newTips, newBreakers

def solution(maze):
    dim = [len(maze), len(maze[0])]
    tips = [[0, 0]]
    covered = [[0, 0]]
    breakers = [True]
    x = 1
    while not [dim[0] - 1, dim[1] - 1] in tips:
        
        x += 1
        tips, covered, breakers = branch(maze, tips, covered, breakers)   
    return x


