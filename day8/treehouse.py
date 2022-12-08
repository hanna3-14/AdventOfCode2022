import re

f = open("treehouse.txt", "r")
lines = f.readlines()

listOfLists = []

totalcount = 0

for line in lines:
	listOfLists.append(list(line))

inverted = list(map(list, zip(*listOfLists)))

# task 1
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

# task 2
scenicscores = []

for i, row in enumerate(listOfLists):
	for j, tree in enumerate(row):
		if (not i == 0) and (not j == 0) and (not j == len(row) - 1) and (not i == len(listOfLists) - 1):
			rowpoints = []
			sublist1 = row[0:j]
			sublist1.reverse()
			sublist2 = row[j + 1:]
			sublist3 = inverted[j][0:i]
			sublist3.reverse()
			sublist4 = inverted[j][i + 1:]
			for k, element in enumerate(sublist1):
				if sublist1[k] >= listOfLists[i][j]:
					rowpoints.append(k + 1)
					break
				elif k == len(sublist1) - 1:
					rowpoints.append(k + 1)
			for k, element in enumerate(sublist2):
				if sublist2[k] >= listOfLists[i][j]:
					rowpoints.append(k + 1)
					break
				elif k == len(sublist2) - 1:
					rowpoints.append(k + 1)
			for k, element in enumerate(sublist3):
				if sublist3[k] >= listOfLists[i][j]:
					rowpoints.append(k + 1)
					break
				elif k == len(sublist3) - 1:
					rowpoints.append(k + 1)
			for k, element in enumerate(sublist4):
				if sublist4[k] >= listOfLists[i][j]:
					rowpoints.append(k + 1)
					break
				elif k == len(sublist4) - 1:
					rowpoints.append(k + 1)
			scenicscores.append(rowpoints[0] * rowpoints[1] * rowpoints[2] * rowpoints[3])

print(max(scenicscores))
