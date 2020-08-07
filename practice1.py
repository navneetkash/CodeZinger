order_of_the_array = int(input())
emp = []
for i in range(order_of_the_array):
    n = list(map(int,input().split()))
    emp.append(n)

result_output = [[sum(int(a)*int(b) for a,b in zip(X_row,X_col)) for X_col in zip(*emp)] for X_row in emp]
if emp == result_output:
    print("Yes")
else:
    print("No")