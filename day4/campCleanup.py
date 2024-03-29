import re

f = open("campCleanup.txt", "r")
lines = f.readlines()

fullyConainedPairs = 0

for line in lines:
	numbers = re.findall(r'\d+', line)

	if (int(numbers[0]) >= int(numbers[2]) and int(numbers[1]) <= int(numbers[3])) or (int(numbers[2]) >= int(numbers[0]) and int(numbers[3]) <= int(numbers[1])):
		fullyConainedPairs += 1

print(fullyConainedPairs)

overlappedPairs = 0

for line in lines:
	numbers = re.findall(r'\d+', line)

	list1 = list(range(int(numbers[0]), int(numbers[1]) + 1))
	list2 = list(range(int(numbers[2]), int(numbers[3]) + 1))

	if len(set(list1).intersection(list2)) != 0:
		overlappedPairs += 1

print(overlappedPairs)
