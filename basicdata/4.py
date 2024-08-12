n = int(input().strip())
s = []

for _ in range(n):
    name = input().strip()
    grade = float(input().strip())
    s.append([name, grade])

g = sorted(set(x[1] for x in s))
slg = g[1]

sl_names = [x[0] for x in s if x[1] == slg]
sl_names.sort()

for name in sl_names:
    print(name)
