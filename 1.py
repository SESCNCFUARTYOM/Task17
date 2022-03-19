count = 0
summ = 0
with open("17.txt", "r") as f:
    lines = [int(i) for i in f]
for i in range(len(lines) - 1):
    if (lines[i] % 3 == 0) or (lines[i+1] % 3 == 0):
        count += 1
        summ = max(summ, lines[i] + lines[i+1])
print(count,summ)