"""
As Commander Lambda's personal assistant, you've been assigned the task of configuring the LAMBCHOP doomsday device's axial orientation gears. It should be pretty simple -- just add gears to create the appropriate rotation ratio. But the problem is, due to the layout of the LAMBCHOP and the complicated system of beams and pipes supporting it, the pegs that will support the gears are fixed in place.

The LAMBCHOP's engineers have given you lists identifying the placement of groups of pegs along various support beams. You need to place a gear on each peg (otherwise the gears will collide with unoccupied pegs). The engineers have plenty of gears in all different sizes stocked up, so you can choose gears of any size, from a radius of 1 on up. Your goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction. Each gear (except the last) touches and turns the gear on the next peg to the right.

Given a list of distinct positive integers named pegs representing the location of each peg along the support beam, write a function solution(pegs) which, if there is a solution, returns a list of two positive integers a and b representing the numerator and denominator of the first gear's radius in its simplest form in order to achieve the goal above, such that radius = a/b. The ratio a/b should be greater than or equal to 1. Not all support configurations will necessarily be capable of creating the proper rotation ratio, so if the task is impossible, the function solution(pegs) should return the list [-1, -1].

For example, if the pegs are placed at [4, 30, 50], then the first gear could have a radius of 12, the second gear could have a radius of 14, and the last one a radius of 6. Thus, the last gear would rotate twice as fast as the first one. In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].

The list pegs will be given sorted in ascending order and will contain at least 2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.
"""

import numpy as np

def gear(pegs, gear):
    for distance in np.diff(np.array(pegs)):
        gear = distance - gear
        print(gear)
    return gear

def verify(pegs, answer):
    rad, denominator = answer
    pegs = np.array(pegs) * denominator
    if rad < denominator:
            return [-1, -1]
    for distance in np.diff(pegs):
        rad = distance - rad
        if rad < denominator:
            return [-1, -1]
    return answer

def solution(pegs):
    # initializing variables
    mathTerms = np.array(pegs)
    numberOfPegs = len(pegs)
    
    # alternating additive inversing
    mathTerms[::2] *= -1

    # double inside
    mathTerms[1:-1] *= 2

    # find last gear radius
    lastGearRad = np.sum(mathTerms)
    
    # get first gear radius
    firstGearRad = lastGearRad * 2
    
    # check if even to decide denominator    
    if numberOfPegs % 2:
        # since there's an odd number of pegs it will just use 1 as denominator
        denominator = 1
    else:
        # since there's an even number of pegs it will divide by 3, but first it needs to check if it can be simplified
        if firstGearRad % 3:
            # since not divissible by 3 it will now just make the denominator 3
            denominator = 3
        else:
            # since it is divissible by 3 it will divide the gear radius by it and make the denominator 1
            denominator = 1
            firstGearRad /= 3

    # invalid checking
    rad = firstGearRad
    if rad < denominator:
        return [-1, -1]
    for distance in np.diff(np.array(pegs) * denominator):
        rad = distance - rad
        if rad < denominator:
            return [-1, -1]
    # return answer
    return [int(firstGearRad), int(denominator)]    


# was on the toilet when I found this solution
def poop(pegs):
    return f'{pegs[-1] - pegs[0] - 2 * (np.sum(np.array(pegs[1:-1]) * -1) + pegs[1])} / 3'
# this solution was naive and also reversed LMAOAO

# took a shower and now I have a new solution
def shower(pegs):
    length = len(pegs)
    joe = pegs[1]

    pegs = np.array(pegs)[::-1]
    print(f'Pegs at the start:\n{pegs}')

    pegs[1:-1] *= 2
    print(f'Pegs after inner pegs are doubled:\n{pegs}')

    pegs[1::2] *= -1
    print(f'Pegs after alternating inner pegs are reversed:\n{pegs}')

    pegs = sum(pegs) * 2
    print(f'Pegs after sum and gear swipy swapy:\n{pegs}')

    if length % 2:
        print('Odd number of terms.')
        answer = [-pegs, 1]
    else:
        print('Even number of terms.')
        if pegs % 3:
            answer = [pegs, 3]
        else:
            answer = [pegs / 3, 1]

    print(f'Current answer:\n{answer}')

    if 0 < answer[0] < joe:
        return answer
    else:
        return [-1, -1]

def shower(pegs):
    length = len(pegs)
    joe = pegs[1]
    og = np.array(pegs)

    pegs = np.array(pegs)[::-1]
    print(f'Pegs at the start:\n{pegs}')

    pegs[1:-1] *= 2
    print(f'Pegs after inner pegs are doubled:\n{pegs}')

    pegs[1::2] *= -1
    print(f'Pegs after alternating pegs are reversed:\n{pegs}')

    pegs = sum(pegs) * 2
    print(f'Pegs after sum and gear swipy swapy:\n{pegs}')

    if length % 2:
        print('Odd number of pegs.')
        answer = [-pegs, 1]
    else:
        print('Even number of pegs.')
        if pegs % 3:
            answer = [pegs, 3]
        else:
            answer = [pegs / 3, 1]

    print(f'Current answer:\n{answer}')

    if 2 * answer[1] <= answer[0] <= joe * answer[1] - answer[1]:
        gear = answer[0]
        thresh = 1
        if answer[1] == 3:
            og *= 3
            gear *= 3
            thresh = 3
        for distance in np.diff(og):
            gear = distance - gear
            if gear < thresh:
                return [-1, -1]
        return [int(answer[0]), answer[1]]
    else:
        return [-1, -1]
    
def depression(pegs, answer):
    gear = answer[0]
    pegs = np.array(pegs)
    if answer[1] == 3:
        pegs *= 3
        gear *= 3
    for distance in np.diff(pegs):
        gear = distance - gear
        if gear < 1:
            return [-1, -1]
    return answer


pegs = [4, 30, 50]
pegs1 = [4, 17, 50]
pegs2 = [0, 3, 6, 12]
pegs3 = [0, 5, 8, 12]
pegs4 = [3, 11, 16, 23, 30]
pegs5 = [3, 36, 40, 46, 55, 70, 89, 112]
