import itertools

part2 = False

f = open("input.txt", "r")
s = f.read()

t = s.split("\n")

def solve():

	stacks_raw = t[0:8]
	rules_raw = t[10:]

	stacks_raw.reverse()

	stacks = [ [] for _ in range(9) ]

	for sr in stacks_raw:
		i = 1
		j = 0
		while i < 36:
			if sr[i] != " ":
				stacks[j].append(sr[i])
			i += 4
			j += 1

	for r in rules_raw:
		rs = r.split(" ")
		cnt = int(rs[1])
		src = int(rs[3])
		dst = int(rs[5])
		if not part2:
			for i in range(cnt):
				el = stacks[src-1].pop()
				stacks[dst-1].append(el)
		else:
			helper = []
			for i in range(cnt):
				el = stacks[src-1].pop()
				helper.append(el)
			for i in range(cnt):
				el = helper.pop()
				stacks[dst-1].append(el)


	for s in stacks:
		print(s.pop(), end = "")
	print()

solve()

part2 = True
solve()

