mx = 0
s = 0
with open("17-18.txt", "r") as f:
    a = [int(i) for i in f]
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if ((a[i] + a[j]) % 80 == 0) and ((a[i] % 50 == 0) or (a[j] % 50 == 0)):
            s += 1
            mx = max(mx, a[i] + a[j])
print(s,mx)