import re

f = open("rockPaperScissors.txt", "r")
lines = f.readlines()

totalsum = 0

for line in lines:
	line = re.sub("\n", "", line)
	letters = line.split(" ")

	sum = 0

	opponentChoice = ""

	if letters[0] == "A":
		opponentChoice = "Rock"
	elif letters[0] == "B":
		opponentChoice = "Paper"
	elif letters[0] == "C":
		opponentChoice = "Scissors"

	myChoice = ""

	if letters[1] == "X":
		myChoice = "Rock"
		sum += 1
	elif letters[1] == "Y":
		myChoice = "Paper"
		sum += 2
	elif letters[1] == "Z":
		myChoice = "Scissors"
		sum += 3
	
	if opponentChoice == myChoice:
		sum += 3
	elif opponentChoice == "Rock" and myChoice == "Paper":
		sum += 6
	elif opponentChoice == "Paper" and myChoice == "Scissors":
		sum += 6
	elif opponentChoice == "Scissors" and myChoice == "Rock":
		sum += 6

	totalsum += sum

print(totalsum)
