number_of_elements = int(input())
n = list(map(int,input().split()))
count = 0
for i in range(number_of_elements):
    for j in range (number_of_elements):
        if i !=j:
            position = n[i]+n[j]
            sum = i+j
            if position ==sum :
                count = count+1
print(count//2)