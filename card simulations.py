#making the dedck of cards
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(2,15):
                self.cards.append(Card(s,v))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

    def show(self):
        for c in self.cards:
            c.show()

class Player:
    def __init__ (self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()



#making a poker hand

def pokerHand(name):
    deck = Deck()
    deck.shuffle()
    user = Player(str(name))
    for i in range(5):
        user.draw(deck)

    return user

    
def handCheck(player):
    suits = []
    values = []
    new = []
    
    for cards in player.hand:
        suits.append(cards.suit)
        values.append(cards.val)
        
    values.sort()
    straight_check = 0
    for i in range(4):
        if values[i] == values[i + 1] - 1:
            straight_check += 1

    if straight_check == 4 or values == [2,3,4,5,14]:
        if all(x==suits[0] for x in suits) == True:
            if values[0] == 10:
                return "Royal Flush"
            else:
                return "Straight Flush"
        else:
            return "Straight"

    if all(x == suits[0] for x in suits) == True:
        return "Flush"

    result = dict((i, values.count(i)) for i in values)
    dupes = list(result.values())

    if dupes.count(4) == 1:
        return "Quads"
    elif dupes.count(3) == 1 and dupes.count(2) == 1:
        return "Full House"
    elif dupes.count(3) == 1:
        return "Three of a Kind"
    elif dupes.count(2) == 2:
        return "Two Pair"
    elif dupes.count(2) == 1:
        return "One Pair"
    else:
        return "High Card"
    


    
def findProb(dic):
    keys = list(dic.keys())
    values = list(dic.values())
    n = sum(values)
    theory = ["50.1177%", "42.2569%", "4.7539%", "2.1128%", "0.3925%", "0.1965%", "0.1441%", "0.02401%", "0.00139%", "0.000154%"]
    print('{0:<20}'.format("Hand") + '{0:<10}'.format("count") + '{0:<20}'.format("Probability") + '{0:<16}'.format("Real Probability"))
    print("*" * 66)
    for i in range(len(keys)):
        print('{0:<20}'.format(keys[i]) +'{0:<10}'.format(str(values[i])) + '{0:<20}'.format(str(round(values[i] / n * 100,4)) + "%") + '{0:<16}'.format(theory[i]))
        
def simulateHands(n):
    results1 = []
    for i in range(n):
        user = pokerHand(str(i))
        results1.append(handCheck(user))
    hands = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush", "Full House", "Quads",  "Straight Flush", "Royal Flush"]
    results = dict((i, results1.count(i)) for i in hands)

    findProb(results)
