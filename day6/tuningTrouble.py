import re

f = open("tuningTrouble.txt", "r")
inputString = f.read()

letters = list(inputString)

# task 1
for i in range(len(letters) - 4):
	if letters[i] != letters[i + 1] and letters[i] != letters[i + 2] and letters[i] != letters[i + 3] and letters[i + 1] != letters[i + 2] and letters[i + 1] != letters[i + 3] and letters[i + 2] != letters[i + 3]:
		print(i + 4)
		break

# task 2
for i in range(len(letters) - 14):
	sublist = letters[i:i + 14]
	seenElements = []
	for j in range(len(sublist)):
		if not sublist[j] in seenElements:
			seenElements.append(sublist[j])

	if len(seenElements) == len(sublist):
		print(i + 14)
		break
