n = int(input())
x = list(map(int,input().split()))
y = len(x)
res = 1
z = [[1 for i in range(2)] for i in range(len(x))]
for i in range(1,y):
    for j in range(i):
        if (x[j] < x[i] and z[i][0] < z[j][1]+1):
            z[i][0] = z[j][1]+1
        if (x[j] > x[i] and z[i][1] < z[j][0]+1):
            z[i][1] = z[j][0]+1
    if res < max(z[i][0], z[i][1]):
        res = max(z[i][0], z[i][1])
print(res)
