f = open("input.txt", "r")
s = f.read()

t0 = list(map(int, (s.split("\n"))))
n = len(t0)

t = []

i = 0
for el in t0:
	t.append((el, i))
	i += 1

def move(i, k):
	if k == 0:
		return
	val = t[i]
	d = 1 if k > 0 else -1
	for j in range(i, i + k, d):
		t[j % n] = t[(j+d) % n]
	t[(i+k) % n] = val

j = 0
for el in t0:
	i = t.index((el, j))
	move(i, el)
	j += 1

i = t.index((0, t0.index(0)))
x = t[(i+1000)%n][0]
y = t[(i+2000)%n][0]
z = t[(i+3000)%n][0]

print(x+y+z)


t = []

i = 0
for el in t0:
	t.append((el * 811589153, i))
	i += 1

for a in range(10):
	j = 0
	for el in t0:
		i = t.index((el * 811589153, j))
		move(i, (el * 811589153) % (n-1))
		j += 1


i = t.index((0, t0.index(0)))
x = t[(i+1000)%n][0]
y = t[(i+2000)%n][0]
z = t[(i+3000)%n][0]

print(x+y+z)
