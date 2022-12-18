
def solve(rounds, div):
	dummy = [([79, 98], lambda a : a * 19, 23, 2, 3), ([54, 65, 75, 74], lambda a : a + 6, 19, 2, 0), ([79, 60, 97], lambda a : a * a, 13, 1, 3), ([74], lambda a : a + 3, 17, 0, 1)]
	inputreal = [([63, 84, 80, 83, 84, 53, 88, 72], lambda a : a * 11, 13, 4, 7), ([67, 56, 92, 88, 84], lambda a : a + 4, 11, 5, 3), ([52], lambda a : a * a, 2, 3, 1), ([59, 53, 60, 92, 69, 72], lambda a : a + 2, 5, 5, 6), ([61, 52, 55, 61], lambda a : a + 3, 7, 7, 2), ([79, 53], lambda a : a + 1, 3, 0, 6), ([59, 86, 67, 95, 92, 77, 91], lambda a : a + 5, 19, 4, 0), ([58, 83, 89], lambda a : a * 19, 17, 2, 1)]

	monkeys = inputreal

	bigmod = 1
	for m in monkeys:
		bigmod *= m[2]

	n = len(monkeys)

	counts = [0] * n

	for i in range(rounds):
		j = 0
		for j in range(n):
			newMonkeys = []
			for k in range(n):
				newMonkeys.append(([] if j == k else monkeys[k][0], monkeys[k][1], monkeys[k][2], monkeys[k][3], monkeys[k][4]))
			for it in monkeys[j][0]:
				counts[j] += 1
				it = monkeys[j][1](it)
				it //= div
				it %= bigmod
				if it % monkeys[j][2] == 0:
					newMonkeys[monkeys[j][3]][0].append(it)
				else:
					newMonkeys[monkeys[j][4]][0].append(it)
			j += 1
			for k in range(n):
				monkeys[k] = newMonkeys[k]

	print(sorted(counts)[-1] * sorted(counts)[-2])

solve(20, 3)
solve(10000, 1)