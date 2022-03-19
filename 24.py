mx = 0
s = 0
with open("17-23.txt", "r") as f:
    a = [int(i) for i in f]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] - a[j]) % 25 == 0) and ((a[i] % 18 == 0) or (a[j] % 18 == 0)):
            s += 1
            mx = max(mx, a[i] - a[j])
print(s,mx)