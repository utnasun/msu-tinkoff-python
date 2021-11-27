def error_exit():
    f = open('output.txt', 'w')
    f.write('ERROR')
    f.close()
    exit()


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return str(self.suit + self.rank)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit


class Deck:
    def __init__(self):
        self.deck = []
        self.size = 0

    def add_top(self, card: Card):
        if card in self.deck:
            error_exit()
        self.deck.append(card)
        self.size += 1

    def add_bottom(self, card: Card):
        if card in self.deck:
            error_exit()
        self.deck.insert(0, card)
        self.size += 1

    def drop_top(self):
        if self.size > 0:
            self.deck.pop()
            self.size -= 1
        else:
            error_exit()

    def drop_bottom(self):
        if self.size > 0:
            self.deck.pop(0)
            self.size -= 1
        else:
            error_exit()

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        res = ""
        for card in reversed(self.deck):
            res += str(card) + " "
        return res


def handler(commands, d: Deck, filename):
    for cmd in commands:
        if cmd[0] == '+':
            d.add_top(Card(cmd[1], cmd[2]))
        if cmd[0] == '^':
            d.drop_top()
        if cmd[0] == '#':
            d.add_bottom(Card(cmd[1], cmd[2]))
        if cmd[0] == '/':
            d.drop_bottom()
    f = open(filename, 'w')
    if d.is_empty():
        f.write('EMPTY')
    else:
        f.write(str(d))
    f.close()


file = open('input.txt', 'r', encoding='utf-8')
text = file.read().splitlines()
file.close()
deck = Deck()
handler(text, deck, "output.txt")
