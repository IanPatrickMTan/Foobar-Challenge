"""
You've been assigned the onerous task of elevator maintenance -- ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.
"""

import numpy as np

def enc(a):
    return np.sum(a * (np.max(a) ** np.arange(3))[::-1], axis = 1), np.max(a)

def dec(a, k):
    b = a // k ** 2
    b = np.vstack((b, (a - b[0] * k ** 2) // k))
    b = np.vstack((b, (a - b[0] * k ** 2 - b[1] * k)))
    return b.T

def compare(v1, v2):
    if v1[0] > v2[0]:
        return v1
    elif v1[0] < v2[0]:
        return v2
    else:
        if v1[1] > v2[1]:
            return v1
        elif v1[1] < v2[1]:
            return v2
        else:
            if v1[2] > v2[2]:
                return v1
            else:
                return v2

def solutionTry1(originalVersions):
    versions = originalVersions[:]
    versionZeros = [0, 0]
    for x in range(len(versions)):
        versions[x] = (list(map(int, versions[x].split('.'))) + versionZeros)[:3]
    versions = np.array(versions)
    versions = np.sum(versions * (np.max(versions) ** np.arange(3))[::-1], axis = 1)
    return np.array(originalVersions)[np.argsort(versions)].tolist()

def greater(ov1, ov2):
    for v1, v2 in zip(ov1, ov2):
        if v1 > v2:
            return ov2, ov1
        if v1 < v2:
            return ov1, ov2
    return ov1, ov2
grev = np.vectorize(greater)

def solution(versions):
    sortedVersions = np.empty(len(versions), dtype=object)
    versionZeros = [-1, -1]
    for x in range(len(versions)):
        sortedVersions[x] = (list(map(int, versions[x].split('.'))) + versionZeros)[:3]
    return sortedVersions

def solve(versions):
    sortedVersions = versions[:]
    versionZeros = [-1, -1]
    for x in range(len(versions)):
        sortedVersions[x] = (list(map(int, versions[x].split('.'))) + versionZeros)[:3]
    rip = False
    sortedVersionsO = []
    print(sortedVersions)
    for x in range(5):
        for x, y in zip(range(len(sortedVersions) - 1), range(1, len(sortedVersions))):
            sortedVersions[x], sortedVersions[y] = greater(sortedVersions[x], sortedVersions[y])
        print('lol', sortedVersionsO, '\n' ,sortedVersions)
        if sortedVersionsO == sortedVersions:
            return sortedVersions
        sortedVersionsO = sortedVersions

def sort(versions):
    s = 0
    versions[s:(len(versions) - s) - (len(versions) - s) % 2 + 1:2], versions[s::2] = grev(versions[s:(len(versions) - s) - (len(versions) - s) % 2 + 1:2], versions[s::2])
    s = 1
    versions[s:(len(versions) - s) - (len(versions) - s) % 2:2], versions[s + 1::2] = grev(versions[s:(len(versions) - s) - (len(versions) - s) % 2 + 1:2], versions[s::2])


t1 = np.array([4, 2, 3, 5, 1, 0]) 


ver = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
ver1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
