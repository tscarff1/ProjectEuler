#   Project Euler problem 54


#   I'm using 'hand rank' as a number to determine how good a hand is, not accounting for high card.
#   The ranks are as follows:
#   0: High card
#   1: One Pair
#   2: Two Pair
#   3: Three of a Kind
#   4: Straight
#   5: Flush
#   6: Full House
#   7: Four of a Kind
#   8: Straight Flush

# A card is a two character string '2H'
def getCardValue(card):
    cardVal = card[:-1]
    if cardVal.isalpha():
        if cardVal == 'T':
            return 10
        if cardVal == 'J':
            return 11
        if cardVal == 'Q':
            return 12
        if cardVal == 'K':
            return 13
        if cardVal == 'A':
            return 14
    else:
        return int(cardVal)


#Currently using bubble sort
def sortCards(cards):
    for i in range(0,len(cards)-1):
        for j in range(i+1, len(cards)):
            iVal = getCardValue(cards[i])
            jVal = getCardValue(cards[j])
            if jVal < iVal:
                tempCard = cards[i]
                cards[i] = cards[j]
                cards[j] = tempCard



#All of the functions to determine the value of a hand assume the hand is sorted
#This is guaranteed to work if hasStraight and hasFlush work
def hasStraightFlush(cards):
    return hasStraight(cards) and hasFlush(cards)

#this is guaranteed to work
def hasFourOfAKind(cards):
    cardVals = []
    for card in cards:
        cardVals.append(getCardValue(card))
    if cardVals.count(cardVals[0]) == 4:
        #Put the value of the four of a kind at the end of the hand so it is used when calculating the hand value
        cards.append(cards[0])
        return True
    elif cardVals.count(cardVals[1]) == 4:
        return True
    else:
        return False

def hasFullHouse(cards):
    cardVals = []
    for card in cards:
        cardVals.append(getCardValue(card))
    if cardVals.count(cardVals[0]) == 2 and cardVals.count(cardVals[2]) == 3:
        return True
    if cardVals.count(cardVals[0]) == 3 and cardVals.count(cardVals[3]) == 2:
        cards.append(cards[0])
        return True
    else:
        return False;

def hasFlush(cards):
    if cards[0][-1] == cards[1][-1] == cards[2][-1] == cards[3][-1] == cards[4][-1]:
        return True
    else:
        return False;


def hasStraight(cards):
    compare = getCardValue(cards[0])
    for i in range(1, len(cards)):
        if getCardValue(cards[i]) - i != compare:
            return False
    return True


def hasThreeOfAKind(cards):
    cardVals = []
    for card in cards:
        cardVals.append(getCardValue(card))
    if cardVals.count(cardVals[0]) == 3 or cardVals.count(cardVals[1]) == 3 or cardVals.count(cardVals[2]) == 3:
        #The third card will always be part of a three of a kind if one exists
        #So we move that to the end of the hand to use in calculating the relevant hand high card
        cards.append(cards[2])
        return True
    return False


def hasTwoPair(cards):
    cardVals = []
    for card in cards:
        cardVals.append(getCardValue(card))
    if cardVals.count(cardVals[0]) == 2 and cardVals.count(cardVals[2]) == 2:
        if cardVals[0] > cardVals[2]:
            cards.append(cards[0])
        else:
            cards.append(cardVals[2])
        return True
    if cardVals.count(cardVals[0]) == 2 and cardVals.count(cardVals[3]) == 2:
        if cardVals[0] < cardVals[3]:
            cards.append(cards[0])
        return True
    if cardVals.count(cardVals[1]) == 2 and cardVals.count(cardVals[3]) == 2:
        if cardVals[1] > cardVals[3]:
            cards.append(cards[1])
        return True


def hasPair(cards):
    cardVals = []
    for card in cards:
        cardVals.append(getCardValue(card))
    for i in range(0,4):
        if cardVals.count(cardVals[i]) == 2:
            cards.append(cards[i])
            return True
    return False


def getHighCardValue(cards):
    return getCardValue(cards[-1])


# A hand will be stored as a list of 5 2-character strings [10H,JH,QH,KH,AH]
def getHandRank(cards):
    if hasStraightFlush(cards):
        return 10
    if hasFourOfAKind(cards):
        return 9
    if hasFullHouse(cards):
        return 8;
    if hasFlush(cards):
        return 7
    if hasStraight(cards):
        return 6
    if hasThreeOfAKind(cards):
        return 5
    if hasTwoPair(cards):
        return 4
    if hasPair(cards):
        return 3
    else:
        return 1


p1Hands = []
p2Hands = []
numLines = 0
with open("poker.txt") as pokerFile:
    for line in pokerFile:
        lineList = line.strip('\n').split()
        p1Hands.append(lineList[0:5])
        p2Hands.append(lineList[5:10])
        numLines += 1

p1Score = 0
p2Score = 0
for i in range(0, numLines):
    sortCards(p1Hands[i])
    sortCards(p2Hands[i])
    print(str(p1Hands[i]) + " : "  + str(p2Hands[i]))
    p1Rank = getHandRank(p1Hands[i])
    p2Rank = getHandRank(p2Hands[i])
    if p1Rank > p2Rank:
        p1Score += 1
        print("p1 wins")
    elif p2Rank > p1Rank:
        p2Score += 1;
        print("p2 wins")
    else:
        p1HighCard = getHighCardValue(p1Hands[i])
        p2HighCard = getHighCardValue(p2Hands[i])
        if p1HighCard > p2HighCard:
            p1Score += 1
            print("p1 wins")
        else:
            p2Score += 1
            print("p2 wins")

print("p1: " + str(p1Score))
print("p2: " + str(p2Score))

#   Todo: Compare hands of the same rank
