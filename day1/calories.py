f = open("calories.txt", "r")
lines = f.readlines()

count = 0

calories = 0

listOfCalories = []

for line in lines:
	if line.strip() != "":
		calories += int(line)
	else:
		listOfCalories.append(calories)
		calories = 0

highestCalories = 0

for i in listOfCalories:
	if i > highestCalories:
		highestCalories = i

print(highestCalories)

listOfCalories.sort()
listOfCalories.sort(reverse=True)
topThree = listOfCalories[0] + listOfCalories[1] + listOfCalories[2]
print(topThree)
