import random
filename = input("input file name:  ")
with open(filename) as f:
	lines = [line for line in f]
x = random.sample(lines, len(lines))
i = 1
for line in x:
	print("{0}/{1}:{2}".format(i, len(x), line.rstrip()))
	i = i + 1
	input()
