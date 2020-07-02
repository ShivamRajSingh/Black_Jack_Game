#code along of black jack game project
import random 

# setting up values for global variables
suits = ('Hearts' , 'Diamonds' , 'Spades' , 'Clubs')
ranks = ('Two' , 'Three' , 'Four' ,'Five' , 'Six' ,"Seven" ,'Eight' , 'Nine' ,'Ten' ,'Jacks' ,'Queen' , 'King')
values = {'Two' :2 , 'Three':3 , 'Four':4 ,'Five':5 , 'Six':6 ,"Seven":7 ,'Eight':8 , 'Nine':9 ,'Ten':10 ,'Jacks':11 ,'Queen':12 , 'King':13}

#take a boolean to describe about the current scenario
playing = True

#Define a card class which can take up the values of attributes of card
class Card():
	def __init__ (self , suit , rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + " of " + self.suit

#Define a deck card which can instantiate and store the 52 card objects

class Deck():
	def __init__ (self):
		#start with an empty list
		self.deck = []
		for suit in suits:
			for rank in ranks:
				c = Card(suit,rank)
				self.deck.append(c)

	def __str__(self):
		#start with an empty string
		deck_comp = ''
		for card in self.deck:
			#keep on adding 
			deck_comp += '\n' + card.__str__()

		return "The deck has : " + deck_comp

	def shuffle(self):
		# import shuffle method from random package to shuffle your deck of cards
		random.shuffle(self.deck)

	def deal(self):
		#deal function deals with the single card present at the moment
		single_card = self.deck.pop()
		return single_card


# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)


#define a Hand class to store the cards of player

class Hand():
	def __init__(self):
		self.cards = [] #start with an ampty list as we did in the Deck class
		self.value = 0 #to store the value of sum of the cards in our hand , starting withzero 
		self.aces = 0

	def add_card(self ,card):
		# card passed in from Deck.deal() --> which is a single card
		self.cards.append(card) #keep on adding the cards drawn from deck 
		self.value += values[card.rank] #it will add up the values by looking in the dictionary for that card value

		#keep a track of aces to adjust it values
		if card.rank == 'Ace':
			self.aces += 1
	def adjust_for_ace(self):

		# By default we're treating ace's value as 11 so now we need to adjust its value
		while self.aces and self.value >21:
			self.value -= 10
			self.aces -=1
		

# test_deck = Deck() #set up a deck
# test_deck.shuffle() # shuffle that deck

# #Set a player
# test_player = Hand()

# #pull a card from a deck 
# pulled_card = test_deck.deal()

# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

class Chips():
	def __init__ (self , total = 100):
		self.total = total
		self.bet = 0

	def win_bet (self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet 


#now define a function for taking bets
def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips would you like to bet ?"))
		except:
			print("Sorry please provide a numeric value")
		else:
			if chips.bet > chips.total:
				print(f"Sorry , you don't have enough chips! You hace : {chips.total}")
			else:
				break

# define a function for taking hits
def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)
	hand.adjust_for_ace

# define a function to ask for user's wish to hit or stand
def hit_or_stand(deck,hand):
	global playing # to control an upcoming while loop

	while True:
		x = input('Hit or Stand ? Enter h or s : ')

		if x[0].lower() == 'h':
			hit(deck,hand)
		elif x[0].lower() == 's':
			print("Player stands , Dealer's turn ")
			playing = False

		else:
			print("Sorry, I didn't get you ")
			continue

# define functions to display cards

def show_some(player , dealer):
	print("Dealer's Hand")
	print("One Card Hdden")
	print(dealer.cards[1])
	print("\n")
	print("Player's Hand:")
	for card in player.cards:
		print(card)

def show_all(player , dealer):
	print("Dealer's Hand")
	for card in delars.cards:
		print(card)
	print("\n")
	print("Player's Hand:")
	for card in player.cards:
		print(card)	

# Now define functions to check whether player lose or win

def player_busts(player,dealer,chips):
	print("BUST PLAYER !!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS!!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("DEALER BUSTED !!")
	chips.lose_bet()

def dealer_wins(player,dealer,chips):
	print("DEALER WINS!!")
	chips.win_bet()

# Here comes the entire logic of playing a game

while True:
	print("Welcome to Black Jack Game designed by - Shivam")

	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())


	#Set up player's chips
	player_chips = Chips()

	# Prompt the player for their bet
	take_bet(player_chips)

	# show cards (but keep one dealer card hidden)
	show_some(player_hand, dealer_hand)

	while playing:
		#Prompt for player to Hit or Stand 
		hit_or_stand(deck,player_hand)

		#show cards (but keep one dealer card hidden)
		show_some(player_hand , dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand , dealer_hand , player_chips)

			break

	if player_hand.value <= 21:

		while dealer_hand.value < player_hand.value:
			hit(deck,dealer_hand)

		#show all cards
		show_all(player_hand , dealer_hand)

		#Run different winning scenario 

		if dealer_hand.value > 21:
			dealer_busts(player_hand , dealer_hand , player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand , dealer_hand , player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand , dealer_hand , player_chips)
		else:
			push(player_hand,dealer_hand)


	#inform player of their total chips
	print('\n Player total chips are at {}'.format(player_chips.total))

	new_game = input("Would you like to play again? y/n")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank You for Playing!")
		break