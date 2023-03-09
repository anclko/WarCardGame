import unittest
from card import Card
from deck import Deck
from intelligence import Intelligence

i = Intelligence()

class IntelligenceTestCase(unittest.TestCase):


    def test_easy(self):
        deck = Deck()
        deck._cards = [Card("Spades", "Q"), Card("Diamonds", "4")]
        card = i.easy(deck)

        self.assertTrue(card, deck._cards)

    def test_hard(self):
        deck = Deck()
        LowerValueCard = Card("Hearts", "7")
        HigherValueCard = Card("Clubs", "K")
        deck._cards = [LowerValueCard, HigherValueCard]

        card = i.hard(deck)

        self.assertEqual(card, HigherValueCard)


if __name__ == '__main__':
    unittest.main()

