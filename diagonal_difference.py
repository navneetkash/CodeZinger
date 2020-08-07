x = int(input())
arr = []
for i in range(x):
    n = list(map(int,input().split()))
    arr.append(n)
sum_diagonal1 = 0
for i in range(x):
    sum_diagonal1 = sum_diagonal1 + arr[i][i]
sum_diagonal2 = 0
for i in range(x):
    sum_diagonal2 = sum_diagonal2 + arr[i][x-i-1]

diff = sum_diagonal1 - sum_diagonal2
print(diff)