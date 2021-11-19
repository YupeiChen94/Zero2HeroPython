from random import shuffle
import time

# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
suits = ('♥', '♦', '♠', '♣')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        try:
            return self.deck.pop()
        except IndexError:
            print('There are no more cards left in the deck')


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        hand_comp = '\nTotal: ' + str(self.value)
        for card in self.cards:
            hand_comp += '\n ' + card.__str__()
        return hand_comp

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?\n'))
        except ValueError:
            print('Sorry, a bet must be an integer!\n')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet cannot exceed', chips.total, '\n')
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal_one())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('Would you like to (H)it or (S)tand?\n')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer is playing.\n')
            playing = False
        else:
            print('Input not accepted, please try again.\n')
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:")
    print("Player's Hand =", player.value)


def player_busts(chips):
    print('Player Busts!')
    chips.lose_bet()


def player_wins(chips):
    print('Player Wins!')
    chips.win_bet()


def dealer_busts(chips):
    print('Dealer Busts!')
    chips.win_bet()


def dealer_wins(chips):
    print('Dealer Wins!')
    chips.lose_bet()


def push():
    print('Dealer and Player tie! It is a push.')


# Print an opening statement
print('\nWelcome to BlackJack! Get as close to 21 as you can without going over! '
      '\nDealer hits until she reaches 17. Aces count as 1 or 11.')
time.sleep(1)
# Set up the Player's chips
player_chips = Chips()

while True:

    # Create & shuffle the deck, deal two cards to each player
    print('Creating and Shuffling Deck...')
    deck = Deck()
    deck.shuffle()
    time.sleep(1)

    print('Dealing cards...')
    dealer_hand = Hand()
    player_hand = Hand()
    for x in range(2):
        dealer_hand.add_card(deck.deal_one())
        player_hand.add_card(deck.deal_one())

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input('Would you like to play another hand? Y/N\n')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break

