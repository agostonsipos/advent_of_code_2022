f = open("input.txt", "r")
s = f.read()

mat = list(map(list, s.split("\n")))

order = ["N", "S", "W", "E"]
elves = {}
x = 0
for l in mat:
	y = 0
	for c in l:
		if c == "#":
			elves[(x,y)] = (x, y)
		y += 1
	x += 1

def stay(x, y):
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if (i, j) != (x, y) and (i, j) in elves.keys():
				return False
	return True

def check(x, y, d):
	match d:
		case "N":
			return (x-1,y-1) not in elves.keys() and (x-1,y) not in elves.keys() and (x-1,y+1) not in elves.keys()
		case "S":
			return (x+1,y-1) not in elves.keys() and (x+1,y) not in elves.keys() and (x+1,y+1) not in elves.keys()
		case "W":
			return (x-1,y-1) not in elves.keys() and (x,y-1) not in elves.keys() and (x+1,y-1) not in elves.keys()
		case "E":
			return (x-1,y+1) not in elves.keys() and (x,y+1) not in elves.keys() and (x+1,y+1) not in elves.keys()

def move(x, y, d):
	match d:
		case "N":
			return (x-1,y)
		case "S":
			return (x+1,y)
		case "W":
			return (x,y-1)
		case "E":
			return (x,y+1)

def part1():
	mx = MX = len(mat) // 2
	my = MY = len(mat) // 2
	for e in elves.keys():
		if e[0] < mx:
			mx = e[0]
		elif e[0] > MX:
			MX = e[0]
		if e[1] < my:
			my = e[1]
		elif e[1] > MY:
			MY = e[1]

	c = (MX - mx + 1) * (MY - my + 1) - len(elves)
	print(c)

for k in range(10000):
	moveHappen = False
	for e in elves.keys():
		if stay(e[0], e[1]):
			continue
		if elves[e] == (e[0], e[1]):
			for d in range(k, k + 4):
				cons = order[d % 4]
				if check(e[0], e[1], cons):
					elves[e] = move(e[0], e[1], cons)
					break
	newelves = {}
	for e in elves.keys():
		mv = elves[e]
		if mv == e:
			newelves[mv] = mv
			continue
		for other in elves.keys():
			if other != e and elves[other] == mv:
				mv = e
				elves[other] = other
				break
		if e != mv:
			moveHappen = True
		newelves[mv] = mv
	if k == 10:
		part1()
	if not moveHappen:
		print(k+1)
		exit()
	elves = newelves
