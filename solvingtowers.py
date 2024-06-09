## Computer solving the towers of hanoi. 3 pegs, 5 rings.

rungs = [[5,4,3,2,1], [], []] # 3 pegs, 5 rings

def solveHanoi3(n, source, target, auxiliary):
    if n > 0: # if there are rings to move 
        solveHanoi3(n-1, source, auxiliary, target) # move n-1 rings from source to auxiliary
        target.append(source.pop()) # move the last ring from source to target
        print(rungs)            # print the current state of the pegs
        solveHanoi3(n-1, auxiliary, target, source) # move n-1 rings from auxiliary to target

solveHanoi3(5, rungs[0], rungs[2], rungs[1])




## Computer solving the towers of hanoi. 4 pegs, 5 rings.

rungs = [[5,4,3,2,1], [], [], []] # 4 pegs, 5 rings

def solveHanoi4(n, source, target, auxiliary):
    if n > 0:
        solveHanoi4(n-1, source, auxiliary, target)
        target.append(source.pop())
        print(rungs)
        solveHanoi4(n-1, auxiliary, target, source)

solveHanoi4(5, rungs[0], rungs[3], rungs[1])
