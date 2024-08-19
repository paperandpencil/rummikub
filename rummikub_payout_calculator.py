'''
TODO 8 Aug 2024

accept input from cmd line # DONE
accept input from file ?

save input from cmdline to file?

######################

Aim of program is to calculate,
how much each player has to pay (or will receive), 
after N games of rummikub.

# AFTER A GAME OF RUMMIKUB
When a game of rummikub finishes, each player has a score.
Each player's score, is the sum of points remaining in their hand/rack.
The player with the minimum sum of points, is the winner.
Note. The winner's score is usually, but not necessarily, zero.

# AMOUNT THAT A PLAYER HAS TO PAY/WILL RECEIVE, AFTER A GAME OF RUMMIKUB
The winner will win the sum of all other player scores.
All other players(ie. losers) will lose a amount equivalent to their individual score.
see sample data entry below for examples.

# DATA INPUT
1st row, number of games played (n_games)

Then for each game of rummikub,
program expects to handle n rows of data, 
formatted as below:

1st row will be the number of players in that game (n_players).
The following n_players rows, 
will have a player's name and their score.

######################

# Start of SAMPLE DATA ENTRY 1
3
4
jsu 40
btan 50
xlow 100
chao 0
4
jsu 30
btan 30
xlow 0
chao 90
4
jsu 100
btan 50
xlow 20
chao 0
# End of SAMPLE DATA ENTRY 1

# explanation for SAMPLE DATA ENTRY 1
# after each game, each player has a final score:
game 1, jsu 40, btan 50, xlow 100, chao 0 # chao wins game 1, she wins +190
game 2, jsu 30, btan 30, xlow 0, chao 90 # xlow wins game 2, he wins +150
game 3, jsu 100 btan 50 xlow 20 chao 0 # chao wins game 3, she wins +170

# program output for SAMPLE DATA ENTRY 1

## payout summary, sorted by player names
btan: -50, -30, -50, total: -130
chao: +190, -90, +170, total: +270
jsu: -40, -30, -100, total: -170
xlow: -100, +150, -20, total: +30

## payout summary, sorted by winner to biggest loser
270, chao
30, xlow
-130, btan
-170, jsu

######################

# SAMPLE DATA ENTRY 2
3
4
jsu 40
btan 50
xlow 100
chao 0
3
jsu 30
btan 30
xlow 0
4
jsu 100
btan 50
xlow 20
chao 0

# explanation for SAMPLE DATA ENTRY 2
game 1, jsu 40 btan 50 xlow 100 chao 0 # chao wins, +190
game 2, jsu 30 btan 30 xlow 0 # xlow wins, +60; NOTE chao had to skip this game
game 3, jsu 100 btan 50 xlow 20 chao 0 # chao wins, +170

## payout summary, sorted by player names
btan: -50, -30, -50, total: -130
chao: +190, +170, total: +360
jsu: -40, -30, -100, total: -170
xlow: -100, +60, -20, total: -60

## payout summary, sorted by winner to biggest loser
360, chao
-60, xlow
-130, btan
-170, jsu

# advanced test case, with MORE THAN ONE WINNER
1
5
jsu 50
btan 50
xlow 100
chao 0
nsim 0

# simple test case, ONE WINNER only
1
4
jsu 50
btan 50
xlow 100
chao 0

'''
def read_game_score():
	'''Read from STDIN, the num of players, and then from each row, each player's name and final score.
	
	Returns: a dictionary with k: v, player name: final score
	'''
	a_game = {} 
	n = int(input()) # num of players this game
	for i in range(n):
		name, score = input().split(' ')
		a_game[name] = int(score)
	return a_game

def print_scores_by_game(games):
	print('\nnum of games:', len(games))
	for i, v in enumerate(games):
		print('game', i, v) # 
		
'''
Accepts a dict as input, ie. the object returned by read_game_score().

Function identifies the minimum score among scores,
and also the names of player(s) with the minimum score.

Function then calculates the pot of winnings contributed by the loser(s),
and then creates a new dict, with player name as key, and sum won/lost as value.

Function returns the new dict.
'''
def calc_game_payout(a_game): # v2
	scores = list(a_game.values())
	min_score = min(scores)
	name_of_winners = [] # expect len[name_of_winners] to be 1, but potentially could be >1
	
	payout_pot = 0
	for k, v in a_game.items():
		if v == min_score:
			name_of_winners.append(k)
		else:
			payout_pot += v

	# sanity check	
	#print("payout pot:", payout_pot)
	#print("game min score:", min_score)
	#print("names of winners:", name_of_winners)

	payout = {}
	for k, v in a_game.items():
		if k in name_of_winners:
			payout[k] = payout_pot / len(name_of_winners) # winner(s) split the pot
		else:
			payout[k] = -v # losers, lose an amount, equivalent to their score
	return (payout)

###############################

if __name__ == '__main__':

# READ INPUT, FROM STDIN
	n = int(input()) # num of games

	games = []
	games_loaded = 0
	while games_loaded < n:
		games.append(read_game_score())
		games_loaded += 1
	
	#print_scores_by_game(games) # to check if data was loaded correctly

# CALCULATE
	payouts = []
	for i in range(len(games)):
		g = games[i]
		p = calc_game_payout(g)
		payouts.append(p)
	
	#print(payouts)

	payout_summary = {}
	players = list(payouts[0]) # generate a list of keys, ie. names of players
	for p in players: # generate an 'empty' dict, ie. payout summary, sorted by player
		payout_summary[p] = 0

	def update_payout_summary(this_game, payout_summary):
		for k, v in this_game.items():
			payout_summary[k] += v

	for i in range(len(payouts)):
		update_payout_summary(payouts[i], payout_summary)

# DISPLAY TO STDOUT
	# sorted by players' name, in lexicographical order
	print('\n#######################################')
	print('PAYOUT SUMMARY: sorted by players\' name')
	print('#######################################')
	#i = 0
	for k, v in sorted(payout_summary.items()):
		if v > 0:
			print(k, "WON", float(v), "!")
		if v == 0:
			print(k, "broke even! Neither WON nor LOST anything...")
		if v < 0:
			print(k, "LOST", float(-v), "...")
		#i += 1
		#if i < len(payout_summary):
		#	print('\n')
	print('#######################################\n')

	# sorted by winner(s) first, and biggest loser last
	print('\n#######################################')
	print('PAYOUT SUMMARY: sorted by winner(s) first, biggest loser last')
	print('#######################################')
	new = {}
	for k, v in payout_summary.items():
		if v not in new:
			new[v] = [k]
		elif v in new:
			tmp = new[v]
			tmp.append(k)
			new[v] = tmp
	
	for k, v in sorted(new.items(), reverse=True):
		if k > 0:
			if len(v) > 1:
				v = sorted(v)
				for i in range(len(v)):
					print(k, 'won by', v[i], '!')
			else:
				print(k, 'won by', v[0], '!')
		if k == 0: # nett zero payout is possible, esp. when more than 1 game is played, eg. won X in game 1, lost X in game 2.
			if len(v) > 1:
				v = sorted(v)
				for i in range(len(v)):
					print(v, 'broke even, ie., neither won nor lost anything')
			else:
				print(v[0], 'broke even, ie., neither won nor lost anything')
		if k < 0:
			if len(v) > 1:
				v = sorted(v)
				for i in range(len(v)):
					print(float(k), "lost by", v[i], '...')
			else:
				print(float(k), "lost by", v[0], '...')
	print('#######################################\n')
