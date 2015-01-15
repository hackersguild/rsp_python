import random
import sys
import string

moves = ['r', 'p', 's']
computerChoice = random.choice(moves)

userChoice = raw_input('\n\tPlease enter (r)ock, (p)aper, (s)cissors: ')
winningPairs = {'r':'s',
				'p':'r',
				's':'p'}
if userChoice == computerChoice:
	print "\n\t\tDraw game!\n"
elif winningPairs[computerChoice] == userChoice:	
	print "\n\t\tYou win"
else:
	print "\n\t\tYou lose"
print "\t\t\tChallenge between: {0} {1} and HUM {2}\n".format(string.capitalize(sys.platform), computerChoice, userChoice)



