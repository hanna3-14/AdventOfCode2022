import re

f = open("rockPaperScissors.txt", "r")
lines = f.readlines()

totalsumTask1 = 0
totalsumTask2 = 0

for line in lines:
	line = re.sub("\n", "", line)
	letters = line.split(" ")

	sumTask1 = 0

	opponentChoice = ""

	if letters[0] == "A":
		opponentChoice = "Rock"
	elif letters[0] == "B":
		opponentChoice = "Paper"
	elif letters[0] == "C":
		opponentChoice = "Scissors"

	# task 1
	myChoice = ""

	if letters[1] == "X":
		myChoice = "Rock"
		sumTask1 += 1
	elif letters[1] == "Y":
		myChoice = "Paper"
		sumTask1 += 2
	elif letters[1] == "Z":
		myChoice = "Scissors"
		sumTask1 += 3
	
	if opponentChoice == myChoice:
		sumTask1 += 3
	elif opponentChoice == "Rock" and myChoice == "Paper":
		sumTask1 += 6
	elif opponentChoice == "Paper" and myChoice == "Scissors":
		sumTask1 += 6
	elif opponentChoice == "Scissors" and myChoice == "Rock":
		sumTask1 += 6

	totalsumTask1 += sumTask1

	# task 2
	neededOutput = ""

	sumTask2 = 0

	if letters[1] == "X":
		neededOutput = "lose"
	elif letters[1] == "Y":
		neededOutput = "draw"
	elif letters[1] == "Z":
		neededOutput = "win"
	
	# 1 for Rock, 2 for Paper and 3 for Scissors
	# 0 for loose, 3 for draw and 6 for win
	if opponentChoice == "Rock" and neededOutput == "lose":
		# I choose Scissors
		sumTask2 += 3 # points for Scissors
	if opponentChoice == "Rock" and neededOutput == "draw":
		# I choose Rock
		sumTask2 += 1 # points for Rock
		sumTask2 += 3 # points for draw
	if opponentChoice == "Rock" and neededOutput == "win":
		# I choose Paper
		sumTask2 += 2 # points for Paper
		sumTask2 += 6 # points for win
	
	if opponentChoice == "Paper" and neededOutput == "lose":
		# I choose Rock
		sumTask2 += 1 # points for Rock
	if opponentChoice == "Paper" and neededOutput == "draw":
		# I choose Paper
		sumTask2 += 2 # points for Paper
		sumTask2 += 3 # points for draw
	if opponentChoice == "Paper" and neededOutput == "win":
		# I choose Scissors
		sumTask2 += 3 # points for Scissors
		sumTask2 += 6 # points for win

	if opponentChoice == "Scissors" and neededOutput == "lose":
		# I choose Paper
		sumTask2 += 2
	if opponentChoice == "Scissors" and neededOutput == "draw":
		# I choose Scissors
		sumTask2 += 3 # points for Scissors
		sumTask2 += 3 # points for draw
	if opponentChoice == "Scissors" and neededOutput == "win":
		# I choose Rock
		sumTask2 += 1 # points for Rock
		sumTask2 += 6 # points for win
	
	totalsumTask2 += sumTask2

print(totalsumTask1)
print(totalsumTask2)
