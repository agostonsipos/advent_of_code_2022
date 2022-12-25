f = open("input.txt", "r")
s = f.read()

y = 0
for l in s.split("\n"):
	x = 0
	for c in l:
		if c == "=":
			x -= 2
		elif c == "-":
			x -= 1
		else:
			x += int(c)
		x *= 5
	x //= 5
	y += x

print(y)

import math

z = int(math.log(2*y, 5))

for i in range(z, -1, -1):
	k = int(5**i)
	if y >= k * 1.5:
		print(2, end="")
		y -= k * 2
	elif y >= k * 0.5:
		print(1, end="")
		y -= k
	elif y <= -k * 1.5:
		print("=", end="")
		y += k * 2
	elif y <= -k * 0.5:
		print("-", end="")
		y += k
	else:
		print(0, end="")

print()
