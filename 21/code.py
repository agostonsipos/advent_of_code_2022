f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

m = []

for l in t:
	a = l.split(": ")
	if len(a) > 1:
		m.append((a[0], a[1].split(" ")))

vals = {}

def eval(name):
	if name in vals.keys():
		return vals[name]
	else:
		for r in m:
			if r[0] == name:
				if len(r[1]) == 1:
					return int(r[1][0])
				else:
					[lhs, op, rhs] = r[1]
					match op:
						case "+":
							return eval(lhs) + eval(rhs)
						case "-":
							return eval(lhs) - eval(rhs)
						case "*":
							return eval(lhs) * eval(rhs)
						case "/":
							return eval(lhs) // eval(rhs)
						case "=":
							return int(eval(lhs) == eval(rhs))
						case default:
							raise "wrong operation"

x = eval("root")
print(x)

def evalLhsWithHumn(x):
	vals = {}
	for r in m:
		if r[0] == "humn":
			r[1][0] = x
	return eval("qhbp")

def part2():
	for r in m:
		if r[0] == "root":
			r[1][1] = "="
	rhs = eval("vglr")
	i = 0
	evalLhsWithHumn(i)
	while True:
		h = 1 << i
		lhs = evalLhsWithHumn(h)
		if lhs <= rhs:
			lower = 1 << (i-1)
			upper = 1 << i
			break
		i += 1
	while True:
		h = (lower + upper) // 2
		lhs = evalLhsWithHumn(h)
		if lhs == rhs:
			for j in range(h - 1, 0, -1):
				vals = {}
				lhs = evalLhsWithHumn(j)
				if lhs != rhs:
					print(j + 1)
					return
		if lhs > rhs:
			lower = h
		else:
			upper = h
		
part2()
