from bigtree import Node, print_tree, find_name
import re

f = open("filesystem.txt", "r")
lines = f.readlines()

root = Node('/')

parentNode = root

listOfDirectories = []

# task 1
for line in lines:
	re.sub("\n", "", line)
	chunks = line.split(' ')

	directorysum = 0

	if not re.match('\$', line) and not re.findall('dir', line): # output of ls
		Node(chunks[0], parent=parentNode)
	elif re.match('\$', line) and re.findall('cd', line) and not re.findall('\.\.', line):
		node = Node(chunks[2], parent=parentNode)
		parentNode = node
	elif re.match('\$', line) and re.findall('cd ..', line):
		for node in parentNode.children:
			if re.match('\d+', node.name):
				directorysum += int(node.name)
		parentNode = parentNode.parent
		Node(str(directorysum), parent=parentNode)
		listOfDirectories.append(directorysum)

print_tree(root)

totalsum = 0

for number in listOfDirectories:
	if number <= 100000:
		totalsum += number

print(totalsum)

# task 2
usedSpace = max(listOfDirectories)
print("used space: ", usedSpace)

availableSpace = 70000000 - usedSpace
print("available space: ", availableSpace)

neededSpace = 30000000 - availableSpace
print("needed space:", neededSpace)
delete = 70000000

for number in listOfDirectories:
	if number >= neededSpace and number < delete:
		delete = number

print("file to delete:", delete)

