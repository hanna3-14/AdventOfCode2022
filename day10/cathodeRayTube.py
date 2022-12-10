import re

f = open("cathodeRayTube.txt", "r")
lines = f.readlines()

x = 1
cycle = 0

totalsum = 0

# task 1
for line in lines:
	re.sub("\n", "", line)
	chunks = line.split(' ')

	if re.match('noop', line):
		cycle += 1
		if cycle % 40 == 20:
			totalsum += cycle * x
	elif re.match('addx', line):
		cycle += 1
		if cycle % 40 == 20:
			totalsum += cycle * x
		cycle += 1
		if cycle % 40 == 20:
			totalsum += cycle * x
		x += int(chunks[1])

print(totalsum)

# task 2
x = 1
sprite = []
grid = [[None] * 40] * 6
i = 0
cycle = 0

for line in lines:
	re.sub("\n", "", line)
	chunks = line.split(' ')

	sprite = [x - 1, x, x + 1]

	if re.match('noop', line):
		if sprite[0] == cycle or sprite[1] == cycle or sprite[2] == cycle:
			grid[i][cycle] = "#"
		else:
			grid[i][cycle] = "."
		cycle += 1
		if cycle == 40:
			for j in range(len(grid[i])):
				print(grid[i][j], end="")
			print("")
			i += 1
			cycle = 0
	elif re.match('addx', line):
		if sprite[0] == cycle or sprite[1] == cycle or sprite[2] == cycle:
			grid[i][cycle] = "#"
		else:
			grid[i][cycle] = "."
		cycle += 1
		if cycle == 40:
			for j in range(len(grid[i])):
				print(grid[i][j], end="")
			print("")
			i += 1
			cycle = 0
		if sprite[0] == cycle or sprite[1] == cycle or sprite[2] == cycle:
			grid[i][cycle] = "#"
		else:
			grid[i][cycle] = "."
		cycle += 1
		if cycle == 40:
			for j in range(len(grid[i])):
				print(grid[i][j], end="")
			print("")
			i += 1
			cycle = 0
		x += int(chunks[1])
