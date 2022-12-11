import re, math

f = open("monkeyInTheMiddle.txt", "r")
lines = f.readlines()

monkeys = []

number = 0
new = 0

# add monkeys to monkeys []
for index, line in enumerate(lines):
	re.sub("\n", "", line)
	chunks = line.split(' ')

	if re.match('Monkey', line):
		number = int(re.sub(":\n", "", chunks[1]))
		monkeys.append([number, 0])

# task 1
for k in range(20):
	for index, line in enumerate(lines):
		re.sub("\n", "", line)
		chunks = line.split(' ')

		if re.match('Monkey', line):
			number = int(re.sub(":\n", "", chunks[1]))
			print('Monkey', monkeys[number][0])
		elif re.findall('Starting items:', line):
			i = 4
			while i < len(chunks):
				item = int(re.sub(",", "", chunks[i]))
				if k == 0:
					monkeys[number].append(item)
				i += 1
		else:
			while len(monkeys[number]) > 2:
				currentItem = monkeys[number].pop(2)
				print("Monkey inspects item:", currentItem)
				monkeys[number][1] += 1
				if re.findall('Operation:', lines[index]):
					if re.findall('\+', lines[index]):
						operationChunks = lines[index].split(' ')
						try:
							operationChunks[7] = int(re.sub("\n", "", operationChunks[7]))
							new = currentItem + int(operationChunks[7])
						except:
							new = currentItem + currentItem
						print("Monkey calculates:", str(currentItem), "+", str(operationChunks[7]))
						new = math.floor(new / 3)
						print("divided:", new)
					elif re.findall('\*', lines[index]):
						operationChunks = lines[index].split(' ')
						try:
							operationChunks[7] = int(re.sub("\n", "", operationChunks[7]))
							new = currentItem * int(operationChunks[7])
						except:
							new = currentItem * currentItem
						print("Monkey calculates:", str(currentItem), "*", str(operationChunks[7]))
						new = math.floor(new / 3)
						print("divided:", new)
				if re.findall('Test:', lines[index + 1]):
					testChunks = lines[index + 1].split(' ')
					if (new % int(testChunks[5])) == 0:
						trueChunks = lines[index + 2].split(' ')
						monkeys[int(trueChunks[9])].append(new)
						print("Throw item", new, "to:", trueChunks[9])
					else:
						falseChunks = lines[index + 3].split(' ')
						monkeys[int(falseChunks[9])].append(new)
						print("Throw item", new, "to:", falseChunks[9])

	print(monkeys)

inspections = []
for i in range(len(monkeys)):
	inspections.append(monkeys[i][1])
print(inspections)

sorted_inspections = sorted(inspections)

most = sorted_inspections[-1]
secondmost = sorted_inspections[-2]

print(most * secondmost)
