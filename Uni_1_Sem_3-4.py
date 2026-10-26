n = int(input("Input a number: "))

list = list(range(1, n + 1))

dick = {}

for i in range(n):
    dick[list[i]] = list[n - 1 - i]

print("List:", list)
print("Dick:", dick)