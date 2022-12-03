f = open("rucksack.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
	string1, string2 = line[:len(line)//2], line[len(line)//2:]

	doubleItem = set(string1).intersection(string2)
	doubleLetter = doubleItem.pop()

	if doubleLetter.isupper():
		sum += ord(doubleLetter) - ord('A') + 27
	else:
		sum += ord(doubleLetter) - ord('a') + 1

print(sum)
