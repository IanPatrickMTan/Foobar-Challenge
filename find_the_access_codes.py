"""
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.
"""

import numpy as np
import itertools as it

def divisible(codes):
    codes = np.array(list(it.combinations(sorted(codes), 2)))
    d1, d2 = codes.T
    codeDic = {}
    for code in codes[np.where(d2 % d1 == 0)]:
        if code[0] in codeDic.keys():
            codeDic[code[0]].append(code[1])
        else:
            codeDic[code[0]] = [code[1]]
    return codeDic

def branch(tips, distances, codeDic):
    newTips = []
    newDistances = []
    for tip, distance in zip(tips, distances):
        if tip in codeDic.keys():
            newTips += codeDic[tip]
            newDistances += [distance + 1] * len(codeDic[tip])
        else:
            newTips.append(tip)
            newDistances.append(distance)
    return newTips, newDistances

def solutionAttempt(numbers):
    numbers = np.array(sorted(numbers))
    codes = []
    for xi, x in enumerate(numbers):
        ynums = np.delete(numbers, xi)
        for yi, y in enumerate(ynums):
            if y % x == 0:
                znums = np.delete(ynums, yi)
                for zi, z in enumerate(znums):
                    if z % y == 0:
                        codes.append([x, y, z])
    return codes

def solutionAttempt1(numbers):
    numbers = np.array(sorted(numbers))
    codes = []
    for xi, x in enumerate(numbers):
        ynums = np.delete(numbers, xi)
        for yi, y in enumerate(ynums):
            if y % x == 0:
                znums = np.delete(ynums, yi)
                for zi, z in enumerate(znums):
                    if z % y == 0:
                        if not [x, y, z] in codes:
                            codes.append([x, y, z])
    return len(codes)

def solutionAttempt2(numbers):
    xnums = np.array(sorted(numbers))
    codes = []
    codeAmount = 0
    for xi, x in enumerate(xnums[:-2]):
        ynums = numbers[xi + 1:]
        for yi, y in enumerate(ynums):
            if y % x == 0:
                znums = ynums[yi + 1:]
                for zi, z in enumerate(znums):
                    if z % y == 0:
                        if not [x, y, z] in codes:
                            codes.append([x, y, z])
                            codeAmount += 1
    return codeAmount

def numpySolution(nums):
    nums = np.array(sorted(nums))
    divisibles = np.zeros(len(nums))
    codes = 0
    for numi, num in enumerate(nums):
        factors = num % nums[:numi] == 0
        divisibles[numi] = np.sum(factors)
        codes += np.sum(divisibles[np.where(factors)])
    return int(codes)

def solution(nums):
    nums = np.array((nums))
    divisibles = np.zeros(len(nums))
    codes = 0
    for numi, num in enumerate(nums):
        factors = num % nums[:numi] == 0
        divisibles[numi] = np.sum(factors)
        codes += np.sum(divisibles[np.where(factors)])
    return int(codes)


def backup(l):
    c = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]
    return count

codes = [1, 2, 3, 4, 5, 6]
codes1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
codes2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
codes3 = list(range(1, 2001))
