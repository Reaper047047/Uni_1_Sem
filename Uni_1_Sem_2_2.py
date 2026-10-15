import math

n = int(input("What is n: "))
sum = 0

for i in range(n, 0-1, -1):
    sum += i
    print(i)
print(sum)