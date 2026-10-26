text = input("Input text: ")

dick = {}

for symbol in text:
    if symbol in dick:
        dick[symbol] += 1
    else:
        dick[symbol] = 1

print(dick)