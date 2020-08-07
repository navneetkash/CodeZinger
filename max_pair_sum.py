x = int(input())
n = list(map(int,input().split()))
max = -10000000
for i in n:
    for j in n:
        if j == i:
            pass
        else:
            sum = j+i
            if sum>max:
                max = sum 
            else:
                pass

print(max)