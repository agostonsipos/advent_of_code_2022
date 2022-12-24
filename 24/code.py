f = open("input.txt", "r")
s = f.read()

mat = list(map(list, s.split("\n")))

walls = set([])

entry = (0,0)
for p in range(0, len(mat[0])):
	if mat[0][p] == ".":
		entry = (0, p)
	else:
		walls.add((0, p))

exit = (0,0)
for p in range(0, len(mat[-1])):
	if mat[-1][p] == ".":
		exit = (len(mat) - 1, p)
	else:
		walls.add((len(mat) - 1, p))

upblizz = set([])
downblizz = set([])
leftblizz = set([])
rightblizz = set([])

for i in range(1, len(mat)-1):
	for j in range(len(mat[i])):
		match mat[i][j]:
			case "#":
				walls.add((i, j))
			case ">":
				rightblizz.add((i,j))
			case "<":
				leftblizz.add((i,j))
			case "^":
				upblizz.add((i,j))
			case "v":
				downblizz.add((i,j))


def canstep(p):
	return p[0] >= 0 and p[1] >= 0 and p[0] < len(mat) and p[1] < len(mat[0]) and not (p in walls or p in upblizz or p in downblizz or p in leftblizz or p in rightblizz)


def update():
	global rightblizz, downblizz, leftblizz, upblizz
	nrblizz = set([])
	for b in rightblizz:
		npos = (b[0], b[1] + 1)
		if npos in walls:
			npos = (b[0], 1)
		nrblizz.add(npos)
	rightblizz = nrblizz
	nlblizz = set([])
	for b in leftblizz:
		npos = (b[0], b[1] - 1)
		if npos in walls:
			npos = (b[0], len(mat[b[0]]) - 2)
		nlblizz.add(npos)
	leftblizz = nlblizz
	nublizz = set([])
	for b in upblizz:
		npos = (b[0] - 1, b[1])
		if npos in walls:
			npos = (len(mat) - 2, b[1])
		nublizz.add(npos)
	upblizz = nublizz
	ndblizz = set([])
	for b in downblizz:
		npos = (b[0] + 1, b[1])
		if npos in walls:
			npos = (1, b[1])
		ndblizz.add(npos)
	downblizz = ndblizz


def sim(start, end, d):
	pos = set([start])
	for i in range(2000):
		update()
		npos = set([])
		for p in pos:
			if canstep(p):
				npos.add(p)
			if canstep((p[0]+1, p[1])):
				npos.add((p[0]+1, p[1]))
			if canstep((p[0]-1, p[1])):
				npos.add((p[0]-1, p[1]))
			if canstep((p[0], p[1]+1)):
				npos.add((p[0], p[1]+1))
			if canstep((p[0], p[1]-1)):
				npos.add((p[0], p[1]-1))
		pos = npos
		if end in npos:
			if d == 1:
				print(i+1)
			if d < 3:
				return (i+1) + sim(end, start, d+1)
			else:
				return i+1


x = sim(entry, exit, 1)
print(x)

