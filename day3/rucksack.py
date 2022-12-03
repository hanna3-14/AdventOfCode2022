import re

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

sum2 = 0

groups = [lines[i:i+3] for i in range(0, len(lines), 3)]

for group in groups:
	rucksack1 = re.sub("\n", "", group[0])
	rucksack2 = re.sub("\n", "", group[1])
	rucksack3 = re.sub("\n", "", group[2])

	commonItem = set(rucksack1).intersection(rucksack2).intersection(rucksack3)
	commonLetter = commonItem.pop()

	if commonLetter.isupper():
		sum2 += ord(commonLetter) - ord('A') + 27
	else:
		sum2 += ord(commonLetter) - ord('a') + 1	

print(sum2)
