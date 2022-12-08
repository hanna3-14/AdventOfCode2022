import re

f = open("treehouse.txt", "r")
lines = f.readlines()

listOfLists = []

totalcount = 0

for line in lines:
	listOfLists.append(list(line))

inverted = list(map(list, zip(*listOfLists)))

for i, row in enumerate(listOfLists):
	row.pop()
	for j, tree in enumerate(row):
		if i == 0:
			totalcount += 1
		elif j == 0:
			totalcount += 1
		elif j == len(row) - 1:
			totalcount += 1
		elif i == len(listOfLists) - 1:
			totalcount += 1
		else:
			sublist1 = row[0:j]
			sublist2 = row[j + 1:]
			sublist3 = inverted[j][0:i]
			sublist4 = inverted[j][i + 1:]
			if (all (x < listOfLists[i][j] for x in sublist1)) or (all (x < listOfLists[i][j] for x in sublist2)) or (all (x < listOfLists[i][j] for x in sublist3)) or (all(x < listOfLists[i][j] for x in sublist4)):
				totalcount += 1

print(totalcount)
