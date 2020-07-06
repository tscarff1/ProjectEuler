#Project Euler - Problem 205
#Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
#Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

#Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

#What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

#Start by calculating the probability of each person rolling each value
#Each person can roll a max of 36, so I'm storing each of their probabilities in an array of this size for easy reference.
#Could optimize memory by eliminating impossible rolls (such as 1,2,3)

def getDiceDist(distribution, numDice, numSides):
    for d in range(1,numSides+1):
        if numDice > 1:
            getDiceDistRec(distribution, numDice -1, numSides, d)
        else:
            distribution[d] += 1

def getDiceDistRec(distribution, numDice, numSides, currentTotal):
    for d in range(1, numSides+1):
        if numDice > 1:
            getDiceDistRec(distribution, numDice - 1, numSides, currentTotal + d)
        else:
            distribution[currentTotal + d] += 1

peterRolls = [0] * 37
getDiceDist(peterRolls, 9, 4)
peterTotal = sum(peterRolls)
peterRollsProb = [x / peterTotal for x in peterRolls]
print(peterRollsProb)

colinRolls = [0]* 37
getDiceDist(colinRolls, 6, 6)
colinTotal = sum(colinRolls)
colinRollsProb = [x / colinTotal for x in colinRolls]
print(colinRollsProb)

#Function to determine the chances Peter will win if colin rolled the given value
def getPeterWinProbability(val):
    if val < 9:
        return 1
    if val == 36:
        return 0
    else:
        winProb = 0
        for prob in peterRollsProb[val+1:37]:
            winProb += prob
        return winProb

print(sum(peterRollsProb))
print(getPeterWinProbability(35))
print("------------------")
peterWins = 0
for itr in range(6,37):
    peterWins += colinRollsProb[itr] * getPeterWinProbability(itr)
    print(str(itr) + ":" + str(colinRollsProb[itr] * getPeterWinProbability(itr)))

print(peterWins)