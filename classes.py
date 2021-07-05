import random

class Pinochle:
    def __init__(self, isDouble):
        self.deck = self.makeDeck(isDouble)
        self.players = [Player(True), Player(False), Player(False), Player(False)]

    def makeDeck(self, isDouble):
        deck = []
        suits = ["Heart", "Diamond", "Spade", "Club"]
        values = ["9", "10", "Jack", "Queen", "King", "Ace"]

        for suit in suits:
            for value in values:
                deck.append(Card(suit,value))
                deck.append(Card(suit,value))
                if(isDouble):
                    deck.append(Card(suit,value))
                    deck.append(Card(suit,value))
        return deck

    def printDeck(self):
        for card in self.deck:
            card.printCard()

    def shuffleDeck(self):
        return random.shuffle(self.deck)

    def promoteTrump(self, trump):
        for card in self.deck:
            if card.suit == trump:
                card.trump = True

    def dealHands(self):
        a = 0
        b = 12
        for player in self.players:
            player.hand = self.deck[a:b]
            a += 12
            b += 12 

    def countMeld(self):
        for player in self.players:
            player.calculateMeld()


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.trump = False

    def __eq__(self, other):
        return (self.suit==other.suit) and (self.value==other.value)

    def __ne__(self, other):
        return not self.__eq__(other)

    def printCard(self):
        if self.value == "10":
            print(f"{self.value[:2]}{self.suit[0]}")
        else:
            print(f"{self.value[0]}{self.suit[0]}")

class Player:
    def __init__(self, isHuman):
        self.isHuman = isHuman
        self.hand = None
        self.meld = 0

    def printHand(self):
        for card in self.hand:
            card.printCard()

    def calculateMeld(self):
        hand = self.hand.copy()
        pinochle = (Card("Spade","Queen") in hand) and (Card("Diamond", "Jack") in hand)
        #Pinochle
        if pinochle:
            self.meld+=4
            #Double Pinochle
            hand.remove(Card("Spade","Queen"))
            hand.remove(Card("Diamond","Jack"))
            pinochle = (Card("Spade","Queen") in hand) and (Card("Diamond", "Jack") in hand)
            if pinochle:
                self.meld+=28

        #Around
        #should be able to do this by generalizing pinochle strategy

        #Marriages
        #should be able to do similar to pinochle, need to think about royals 
            #-- royals necessitate a meld calculation pre (for bidding logic) and post (for actual score)

        #Book
        #similar to around but static suit, dynamic value