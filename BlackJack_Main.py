"""
Black Jack game.
by @ravi_hir
"""
import random


class person:
	cards = []
	def __init__(self,p_or_d='p'):

		self.p_or_d = p_or_d

		if self.p_or_d == 'p':
			self.balance = int(input('Hey Player, Before we start game, tell me how much money u hv?: '))

	def bet(self):

		self.bet_amount = int(input(f'you hv {self.balance}. How much u want to bet: '))
		return self.bet_amount


class Deck:

    deck = []

    def __init__(self):
        self.deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4
        random.shuffle(self.deck)
        pass

    def deck_shuffle(self):
        random.shuffle(self.deck)

    def serve_card(self):
        return self.deck.pop()

def play_again():
	
	ans = input('If u want to play again from Starting with New Balance, Enter "yes", else anything else: ')
	if ans == 'yes':
		return True
	else:
		return False

def total_value(L):
	sum = 0
	no_of_ace_in_L = L.count(1)
	for i in L:
		if i in [11,12,13]:
			sum +=10
		else:
			sum += i

	if sum > 21 and no_of_ace_in_L>0: # need further work
		sum -= 10 
	return sum

def display(l1, l2):

	print(f"Player's cards: {l1} ")
	print(f"Dealer's cards: {l2} ")

def blackjack(l1):
	return ((set(l1) == {1,11}) or (set(l1) == {1,12}) or (set(l1) == {1,13})

while True:


	player = person()
	dealer = person('d')

	new_deck = Deck()

	#this_game()

	while player.balance > 0:

		#player.bet()
		if(input('If you want to continue, press "y" :') != 'y'):
		break

		while player.bet() > player.balance:
			print('player.bet_amount > player.balance.')

		p_list=[]
		p_list.append(new_deck.serve_card())
		p_list.append(new_deck.serve_card())


		d_list=[]
		d_list.append(new_deck.serve_card())
		d_list.append(new_deck.serve_card())

		display(p_list, d_list)

		if blackjack(p_list):
			if blackjack(d_list):
				print('No one Wins')
				display(p_list, d_list)
				continue
			else:
				print(f'Player wins. gets 1.5 X {player.bet_amount}.')
				player.balance += 1.5 * player.bet_amount
				print(f'New Balance is {player.balance}')
				continue

		if (total_value(p_list) > 21):

			print('Player busted : {p_list}')
			player.balance -= player.bet_amount
			print(f'After diducting {player.bet_amount}, new balance is {player.balance}')
			continue

		

		if total_value(p_list) == 21:

			if(total_value(d_list) == 21):
				print('Draw')
				continue
			else:
				player.balance += player.bet_amount
				print(f'player wins {player.bet_amount}. New Balance is : {player.balance}')
				continue
		
			
		print(f'Total value of player cards is: {total_value(p_list)} < 21.\nYou can HIT or STAND')	
		choice = input('Enter "hit" or "stand" :')
		
		while choice == 'hit':
			p_list.append(new_deck.serve_card())
			display(p_list, d_list)
			if total_value(p_list) > 21:
				print('Player busted')
				player.balance -= player.bet_amount
				print(f'After Busting, {player.bet_amount} you hv {player.balance}')
				break
			
			elif total_value(p_list) == 21
				player.balance += player.bet_amount
				print(f'player wins {player.bet_amount}. New Balance is : {player.balance}')
				break
			else:
				print(f'Total value of player cards is: {total_value(p_list)} < 21.\nYou can HIT or STAND')	
				choice = input('Enter "hit" or "stand" :')
			continue
		

		if total_value(p_list) < total_value(d_list):
			print('dealer Won.')
			player.balance -= player.bet_amount
			print(f'After loosing {player.bet_amount} you hv {player.balance}')
			continue	

		while total_value(p_list) >= total_value(d_list) and total_value(d_list) <21:
			d_list.append(new_deck.serve_card())

		if total_value(p_list) < total_value(d_list):
			print('dealer Won.')
			player.balance -= player.bet_amount
			print(f'After loosing {player.bet_amount} you hv {player.balance}')
			continue
		else:
			print('dealer busted')
			player.balance += player.bet_amount
			print(f'After wining {player.bet_amount} you hv {player.balance}')
			continue

else:
	print('you hv ZERO balance. U looser.')
	if play_again() == False:
		print('Lets END. Good Night :)')
