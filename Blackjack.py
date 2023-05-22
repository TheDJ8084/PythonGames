import random

# Card ranks, suits, and values
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["♠", "♣", "♦", "♥"]
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

# Card class
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank}{self.suit}"

# Deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal_card(self):
        return self.deck.pop()

# Hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "A":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Game logic
def blackjack_game():
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())

    def display_table(show_all=False):
        print("\nDealer's Hand:")
        if show_all:
            for card in dealer_hand.cards:
                print(card, end=" ")
            print(f"\nValue: {dealer_hand.value}")
        else:
            print(dealer_hand.cards[0], " **hidden card**")

        print("\nPlayer's Hand:")
        for card in player_hand.cards:
            print(card, end=" ")
        print(f"\nValue: {player_hand.value}")

    def player_hit_or_stand():
        while True:
            choice = input("\nDo you want to Hit or Stand? Enter 'h' or 's': ").lower()
            if choice == "h":
                player_hand.add_card(deck.deal_card())
                player_hand.adjust_for_ace()
                display_table()
                if player_hand.value > 21:
                    print("Player busts! Dealer wins.")
                    return False
            elif choice == "s":
                return True
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    # Game loop
    while True:
        display_table()

        if player_hand.value == 21:
            print("Player wins with Blackjack!")
            return True

        if player_hit_or_stand():
            while dealer_hand.value < 17:
                dealer_hand.add_card(deck.deal_card())
                dealer_hand.adjust_for_ace()
                display_table(show_all=True)

                if dealer_hand.value > 
