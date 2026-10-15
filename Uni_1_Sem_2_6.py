n = float(input("Enter a number: "))

print("You entered: "+str(n))
if n in range(1, 11):
    print("The number is in the range of 1 to 10")
else:
    print("The number is outside the range of 1 to 10")