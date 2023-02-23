class Player:

    def __init__(self, name):
        self._name = name
        self._deck = []
        self.win = 0

    '''Setters'''
    def set_name(self, name):
        self._name = name

    '''Getters'''
    @property
    def get_name(self):
        return self._name
    
    def win(self,player):
        self.win += 1

    '''return T or F if deck is empty'''
    def has_empty_deck(self):
        return self._deck.size == 0


    '''draw card if the deck is not empty'''
    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()


    '''Deck from Player class, Draw method from Deck class'''
    def add_card(self, card):
        self._deck.add(card)
