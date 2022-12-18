f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

res = 0
c = 0
x = 1

def checkAndUpdate():
	global res
	if c % 40 == 20:
		res += x * c

for l in t:
	cmd = l.split(" ")
	if cmd[0] == "noop":
		c += 1
		checkAndUpdate()
	elif cmd[0] == "addx":
		y = int(cmd[1])
		for i in range(2):
			c += 1
			checkAndUpdate()
		x += y

print(res)

c = 0
x = 1

table = [[" "] * 40, [" "] * 40, [" "] * 40, [" "] * 40, [" "] * 40, [" "] * 40]

def draw():
	if x-1 <= c%40 and c%40 <= x+1:
		table[c//40][c%40] = '='

for l in t:
	cmd = l.split(" ")
	if cmd[0] == "noop":
		draw()
		c += 1
	elif cmd[0] == "addx":
		y = int(cmd[1])
		for i in range(2):
			draw()
			c += 1
		x += y

for l in table:
	print("".join(l))

