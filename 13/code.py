f = open("input.txt", "r")
s = f.read()

t = s.split("\n\n")

def compare(l, r):
	if not isinstance(l, list) and not isinstance(r, list):
		if l < r:
			return -1
		elif l == r:
			return 0
		else:
			return 1
	elif isinstance(l, list) and isinstance(r, list):
		if len(l) == 0 and len(r) == 0:
			return 0
		if len(l) == 0 and len(r) != 0:
			return -1
		elif len(r) == 0 and len(l) != 0:
			return 1
		else:
			c = compare(l[0], r[0])
			if c != 0:
				return c
			else:
				return compare(l[1:], r[1:])
	elif isinstance(l, list) and not isinstance(r, list):
		return compare(l, [r])
	elif not isinstance(l, list) and isinstance(r, list):
		return compare([l], r)

i = 1
s = 0
arr = []
for l in t:
	pair = l.split("\n")
	lhs = eval(pair[0])
	rhs = eval(pair[1])
	arr.append(lhs)
	arr.append(rhs)
	if compare(lhs, rhs) == -1:
		s += i
	i += 1

print(s)

arr.append([[2]])
arr.append([[6]])

i = 1
j = 1
for el in arr:
	if compare(el, [[2]]) == -1:
		i += 1
	if compare(el, [[6]]) == -1:
		j += 1

print(i * j)
