import random



class Card:
    def __init__(self,v,s):
        self.suits = ["spades",'hearts','diamonds','clubs']
        self.values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        self.value = v
        self.suit = s
    
    def __repr__(self) -> str:
        st = f"{self.values[self.value]} of {self.suits[self.suit]}"
        return st
    
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        elif self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False
    
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i,j))
        random.shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

class Player:
    def __init__(self,name):
        self.name =  name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1 = input("p1 name: ")
        name2 = input("p2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def print_draw(self,p1n,p1c,p2n,p2c):
        print(f"{p1n} drew {p1c}, {p2n} drew {p2c}")

    def play_game(self):
        cards = self.deck.cards
        print('beginning the game/war')
        print(cards)
        while len(cards)>0:
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.print_draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                print(f"{p1n} wins the round")
                self.p1.wins+=1
            elif p1c< p2c:
                print(f"{p2n} wins the round")
                self.p2.wins+=1
        winner = self.winner_name()
        print(f'{self.p1.name} won {self.p1.wins}, {self.p2.name} won {self.p2.wins}')
        print(f'winner is {winner}')

    def winner_name(self):
        if self.p1.wins > self.p2.wins:
            return self.p1.name
        elif self.p1.wins < self.p2.wins:
            return self.p2.name
        else:
            print("game over, it was tie!")
            


if __name__ == '__main__':
    # deck = Deck()
    # print(deck.cards)
    # print(len(deck.cards))
    game = Game()
    game.play_game()

