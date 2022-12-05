import re

f = open("supplyStacks.txt", "r")
lines = f.readlines()

stacks = lines[:8]
instructions = lines[10:]

stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []

for crate in stacks:
	stack1.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack2.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack3.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack4.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack5.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack6.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack7.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack8.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]
	stack9.append(re.sub("[\[\n\]\s]*", "", crate[:4]))
	crate = crate[4:]

stack1 = list(filter(None, stack1))
stack2 = list(filter(None, stack2))
stack3 = list(filter(None, stack3))
stack4 = list(filter(None, stack4))
stack5 = list(filter(None, stack5))
stack6 = list(filter(None, stack6))
stack7 = list(filter(None, stack7))
stack8 = list(filter(None, stack8))
stack9 = list(filter(None, stack9))
stack = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

# task 1
#for instruction in instructions:
#	numbers = re.findall(r'\d+', instruction)

#	for i in range(int(numbers[0])):
#		if stack[int(numbers[1]) - 1]:
#			stack[int(numbers[2]) - 1] = [stack[int(numbers[1]) - 1][0]] + stack[int(numbers[2]) - 1]
#		if stack[int(numbers[1]) - 1]:
#			stack[int(numbers[1]) - 1].pop(0)

#print(stack[0][0],stack[1][0],stack[2][0],stack[3][0],stack[4][0],stack[5][0],stack[6][0],stack[7][0],stack[8][0])

# task 2
for instruction in instructions:
	numbers = re.findall(r'\d+', instruction)

	movingList = []
	movingCount = int(numbers[0])

	while movingCount > 0:
		if stack[int(numbers[1]) - 1]:
			movingList.append(stack[int(numbers[1]) - 1][0])
			stack[int(numbers[1]) - 1].pop(0)
		movingCount -= 1

	stack[int(numbers[2]) - 1] = movingList + stack[int(numbers[2]) - 1]

print(stack[0][0],stack[1][0],stack[2][0],stack[3][0],stack[4][0],stack[5][0],stack[6][0],stack[7][0],stack[8][0])
