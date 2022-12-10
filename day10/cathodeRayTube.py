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
