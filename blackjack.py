'''

Create a deck of 52 cards
Shuffle the deck
Ask the Player for their bet
Make sure that the Player's bet does not exceed their available chips
Deal two cards to the Dealer and two cards to the Player
Show only one of the Dealer's cards, the other remains hidden
Show both of the Player's cards
Ask the Player if they wish to Hit, and take another card
If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
Determine the winner and adjust the Player's chips accordingly
Ask the Player if they'd like to play again

'''



from random import shuffle





suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}

player = True

class card():
    
    def __init__(self,suit , rank) -> None:
        self.rank = rank
        self.suit = suit
        self.values = values[rank]
    
    def __str__(self) -> str:
        return self.rank + " of " + self.suit

class deck():

    def __init__(self):
        self.deck = []
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit,rank))
    
    def __str__(self) -> str:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: "+deck_comp

    def shuffle_card(self):
        shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class hand:
    def __init__(self) -> None:
        self.cards= []
        self.value = 0 
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        #while self.value greater than 21 and if i still have an ace 
        # than change ace from 11 to 1  
        while self.value > 21 and self.aces:#it is as while self.value > 21 and self.aces > 0:
            self.value -= 10# making ace as 1 
            self.aces -= 1


class chips:
    def __init__(self,total =100) -> None:
        self.total = total #this can set to a default value or supplied by a user i\p
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



def take_bet(chips):
    while True:
        try:
            chips.bet =int(input("How many chips would you like to bet? "))
        except:
            print("Sorry please enter intger only")
        else:
            if chips.bet > chips.total:
                print("Sorry. You don't have that many chips!!\n You have: {}".format(chips.total))
            else:
                break


#take one card add to hand and check for ace
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

playing = True

def hit_or_stand(deck,hand):
    global playing
    playing =True
    
    while True:
        x = input('Hit or Stand? \nEnter h or s only: ')

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn!!")
            playing = False
        else:
            print("Sorry ,Wrong Input !!\n Please enter only s or h only!!")
            continue
        break


def show_some(player,dealer):

    #show only one card of dealer hand
    print("\nDealer's Hand: ")
    print("Frist card is hidden!!")
    print(dealer.cards[1])
    
    #show all of card's of player
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    #show only one card of dealer hand
    print("\nDealer's Hand: ",*dealer.cards,sep='\n')#it will print "\nDealer's Hand: " then it will at a time one card after that it will add '\n' and then second So on...
    #the above line is same as below  
    # for card in dealer.cards:
    #     print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")
    
    #show all of card's of player
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Dealer's hand is: {dealer.value}")


def player_busts(player,dealer,chips):
    print("BUST PLAYER!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player WINS")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player WINS :) DEALER BUSTED :(")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer WINS")
    chips.lose_bet()


def push(player,dealer,chips):
    print("Dealer and Player tie! PUSH")





#main loop to run game 
while True:
    # Print an opening statement
    print("Lets Play BlackJack!!")
    
    # Create & shuffle the deck
    Deck = deck()
    Deck.shuffle_card()

    #deal two cards to player & dealer
    player_hand = hand()
    player_hand.add_card(Deck.deal())
    player_hand.add_card(Deck.deal())

    dealer_hand = hand()
    dealer_hand.add_card(Deck.deal())
    dealer_hand.add_card(Deck.deal())
    
    # Set up the Player's chips
    player_chips = chips()
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(Deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)

        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    
    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <21:
        while dealer_hand.value < player_hand.value:
            hit(Deck,dealer_hand)
    
        # Show all cards
        show_all(player_hand,dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value >21 :
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
    # Inform Player of their chips total 
    print('\n Player total chips are : {}'.format(player_chips.total))

    # Ask to play again
    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!!\nSee another time!!")
        break


