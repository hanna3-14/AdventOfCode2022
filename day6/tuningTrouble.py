import re

f = open("tuningTrouble.txt", "r")
inputString = f.read()

letters = list(inputString)

for i in range(len(letters) - 4):
	if letters[i] != letters[i + 1] and letters[i] != letters[i + 2] and letters[i] != letters[i + 3] and letters[i + 1] != letters[i + 2] and letters[i + 1] != letters[i + 3] and letters[i + 2] != letters[i + 3]:
		print(i + 4)
		break
