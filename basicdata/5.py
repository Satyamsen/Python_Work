n = int(input().strip())
s_marks = {}
for i in range(n):
    n, *m = input().strip().split()
    s_marks[n] = list(map(float, m))

q_name = input().strip()
avg = sum(s_marks[q_name]) / len(s_marks[q_name])
print(f"{avg:.2f}")
