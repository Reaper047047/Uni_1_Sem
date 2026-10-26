import random

random_chisla = int(input("Give a number: "))

list = []

for i in range(random_chisla):
    list.append(random.randint(1, 100000))

print("Parvo list:", list)

list1 = []

for i in range(len(list) - 1):
    list1.append(list[i])
    list1.append(list[i] + list[i + 1])

list1.append(list[-1])

print("Nov list:", list1)