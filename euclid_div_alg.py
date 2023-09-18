a = int(input("The larger of the 2 numbers: "))
b = int(input("The smaller of the 2 numbers: "))

while b > 0:
    temp = b
    b = a % b
    a = temp

print(a)

