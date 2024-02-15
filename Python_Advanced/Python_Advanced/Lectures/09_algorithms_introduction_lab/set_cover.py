universe = {int(x) for x in input().split(', ')}
num = int(input())
sets = [{int(x) for x in input().split(', ')} for _ in range(num)]
taken_sets = []

while universe:
    best_set = max(sets, key=lambda s: len(universe.intersection(s)))
    taken_sets.append(best_set)
    universe -= set(best_set)

for i in range(len(taken_sets)):
    taken_sets[i] = sorted(taken_sets[i])

print(f"Sets to take ({len(taken_sets)}):")
[print("{ " + f"{', '.join(str(x) for x in s)}" + " }") for s in taken_sets]
