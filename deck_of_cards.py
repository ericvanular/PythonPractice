#implement a full deck of cards, with the ability to deal and shuffle a deck

from random import random as random

class deck_of_cards:
    def __init__(self):
        card_nums = [i for i in range(2,11)]
        card_nums.extend(['K','Q','J','A'])
        self.card_nums = card_nums
        self.card_suits = ['d','h','s','c']
        self.deck = self.gen_deck()
    def gen_deck(self):
        deck = []
        for num in self.card_nums:
            for suit in self.card_suits:
                deck.append(str(num) + suit)
        return deck
    def shuffle(self):
        for i in range(51, 0, -1):
            self.swap(i, (int(random() * 52) // 1 % i))
    def swap(self, idx1, idx2):
        temp = self.deck[idx1]
        self.deck[idx1] = self.deck[idx2]
        self.deck[idx2] = temp
    def deal_hand(self, hand_size):
        hand = []
        for i in range(hand_size):
            hand.append(self.deck[i])
        return hand



deck = deck_of_cards()
print deck.deck
deck.shuffle()
print deck.deck
print deck.deal_hand(5)
deck.shuffle()
print deck.deal_hand(5)