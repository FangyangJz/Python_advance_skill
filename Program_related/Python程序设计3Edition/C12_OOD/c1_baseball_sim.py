
def printIntro():
    print('This program simulates a game of racquetabll between two')
    print('Players called "A" and "B". The ability of each player is')
    print('indicated by a probability(a number between 0 and 1) that')
    print('the player wins the point when serving. Player A always')
    print('has the first serve.')

def getInput():
    # Returns the three simulation parameters probA, proB and n
    a = float(input('What is the prob. player A wins a serve?'))
    b = float(input('What is the prob. player B wins a serve?'))
    n = int(input('How many games to simulate?'))
    return a, b, n

def simNGame(n, probA, probB):
    # simulates n games and returns winsA and winsB
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, socreB = simOneGame(probA, probB)
        if scoreA > socreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    erving = 'A'
    while not gameOver(scoreA, scoreB):
        

def main():
    printIntro()
    probA, probB, n = getInput()
    winsA, winsB = simNGame(n, probA, probB)
    printSummary(winsA, winsB)

if __name__ == '__main__':
    main()