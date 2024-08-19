I like to play rummikub with family. 

Usually, we add a minor monetary component to our play, aka social gambling, just to spice things up.
There is however, a 'pain point' at the end of our games, and that is to determine who won/lost, and by how much.
Manual calculation via paper and pencil takes time, and can be prone to errors.

So the aim of this program is to automate the calculation of how much each player has won/lost, in total, after n games.

# AFTER A GAME OF RUMMIKUB
When a game of rummikub finishes, each player has a score.
Each player's score, is the sum of points remaining in their hand/rack.
The player with the lowest/minimum score, is the winner.
Note 1. The winning score is usually, but not necessarily, zero.
Note 2. It might also be possible, but rare, to have more than one winner. 
I personally have only encountered one game so far, where 2 people tied with the same minimum, albeit non-zero, score. 

# AMOUNT THAT A PLAYER HAS TO PAY/WILL RECEIVE, AFTER A GAME OF RUMMIKUB
The winner will win the sum of all other player scores.
All other players (ie. the losers) will lose a amount equivalent to their individual score.

# KEEP TRACK OF PAYOUTS, ACROSS MULTIPLE GAMES
Sometimes, people are late, and only join in after we have finished a few games.
Sometimes, people have to leave early, while the rest continue to play.

The program is able to handle all these cases!
It generates a payout summary, sorted in TWO ways:
  sorted by player names
  sorted by amount won/lost, ie. biggest winner first, and biggest loser last

Anyway, after we settle the accounts, the winners usually only win what we call 'coffee money'...
