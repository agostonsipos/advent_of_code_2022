f = open("input.txt", "r")
s = f.read()

t = s.split("\n")


x = 0
y = 0
for l in t:
	p = l.split(",")
	[a,b] = p[0].split("-")
	[c,d] = p[1].split("-")
	a = int(a)
	b = int(b)
	c = int(c)
	d = int(d)
	if (c <= a and b <= d) or (a <= c and d <= b):
		x += 1
	if (c <= a and a <= d) or (c <= b and b <= d) or (a <= c and d <= b):
		y += 1

print(x)
print(y)