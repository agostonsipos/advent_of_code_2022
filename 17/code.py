f = open("rocks.txt", "r")
s = f.read()

t = s.split("\n\n")

rocks = []

for r in t:
	rocks.append([])
	for l in r.split("\n"):
		rocks[-1].append(list(l))

f = open("input.txt", "r")
s = f.read()

def collides(world, x, y, r):
	for i in range(0, len(r)):
		for j in range(0, len(r[i])):
			if y < i or x < 0 or x+j >= 7 or (world[y - i][x + j] == "#" and r[i][j] == "#"):
				return True
	return False

def stop(world, x, y, r):
	for i in range(0, len(r)):
		for j in range(0, len(r[i])):
			if r[i][j] == "#":
				world[y - i][x + j] = "#"

statuses = []

def sim(N):
	world = [[" "] * 7 for _ in range(260000)]
	top = -1
	pid = 0
	global statuses
	statuses = []
	for i in range(N):
		rock = rocks[i % 5]
		x = 2
		y = top + 3 + len(rock)
		while True:
			push = s[pid % len(s)]
			dx = 1 if push == ">" else -1
			if not collides(world, x+dx, y, rock):
				x += dx
			pid += 1
			if collides(world, x, y - 1, rock):
				stop(world, x, y, rock)
				top = max(top, y)
				break
			else:
				y -= 1
		statuses.append((x, i % 5, pid % len(s)))
	return top + 1

t = sim(2022)
print(t)

sim(5000) # to get enough data for part2

def findloop():
	for i in range(0, len(statuses)):
		for j in range(i+1, len(statuses)-(len(statuses)-i)//2):
			if statuses[i] == statuses[j] and statuses[j] == statuses[j+j-i]:
				return (i,j-i)

(a,b) = findloop()

N = (1000000000000 - a) // b
M = (1000000000000 - a) % b

x = sim(a)
y = sim(a+b)
z = sim(a+M)

print(x + N * (y-x) + (z-x))
