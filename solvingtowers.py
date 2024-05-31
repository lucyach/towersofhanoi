## Computer solving the towers of hanoi. 3 rungs, 5 rings.

rungs = [[5,4,3,2,1], [], []]

def solveHanoi3(n, source, target, auxiliary):
    if n > 0:
        solveHanoi3(n-1, source, auxiliary, target)
        target.append(source.pop())
        print(rungs)
        solveHanoi3(n-1, auxiliary, target, source)

solveHanoi3(5, rungs[0], rungs[2], rungs[1])

## Computer solving the towers of hanoi. 4 rungs, 5 rings.

rungs = [[5,4,3,2,1], [], [], []]

def solveHanoi4(n, source, target, auxiliary):
    if n > 0:
        solveHanoi4(n-1, source, auxiliary, target)
        target.append(source.pop())
        print(rungs)
        solveHanoi4(n-1, auxiliary, target, source)

solveHanoi4(5, rungs[0], rungs[3], rungs[1])

