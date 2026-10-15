min = int(input("Enter a min: "))
max = int(input("Enter a max: "))
count = 0

for i in range(10):
    n = int(input("Enter a number: "))
    if min <= n <= max:
        count += 1

print(count)