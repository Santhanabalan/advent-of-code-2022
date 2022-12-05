input_data = open('input.txt').read()
data = [part.splitlines() for part in input_data.split('\n\n')]
calories = [sum([int(val) for val in i]) for i in data]
print("Part 1:" ,max(calories))
print("part1 2:" ,sum(sorted(calories, reverse=True)[:3]))