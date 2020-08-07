def solution(L):
    max = 0
    for i in L:
        for j in L:
            if i < j:
                temp = i%j
            else:
                temp = j%i
            if temp > max:
                max = temp
    return max


N=int(input())
L=[]

n=0
for e in input().split():
    if (n<N):
 2       L.append(int (e) )
        n+=1
print(solution(L))

                    