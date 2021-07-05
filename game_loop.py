from classes import Pinochle, Card

class game_loop:
    def __init__(self, isDouble):
        self.pinochle = Pinochle(isDouble)

    def play(self):
        self.deal()
        self.evaluateMeld()

    #deal
    def deal(self):
        print("DEALING CARDS...")
        self.pinochle.shuffleDeck()
        self.pinochle.dealHands()
        #self.pinochle.players[0].printHand()
    
    #evaluate meld
    def evaluateMeld(self):
        print("EVALUATING MELD...")
        self.pinochle.countMeld()


    #bid

    #tricks

    #score