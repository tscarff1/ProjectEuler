products = []

def isPandigitalMultiple(n1, n2) :
    n3 = n1 * n2
    digits = str(n1) + str(n2) + str(n3)
    checked = []
    for digit in digits:
        if digit == "0":
            return False
        elif digit not in checked:
            checked.append(digit)
        else:
            return False

    return True


for i in range(12,99):
    for j in range(123,988):
        if isPandigitalMultiple(i,j) and (i*j) not in products:
            products.append(i*j)
            print(str(i) + " * " + str(j) + " = " + str(i*j))

for i in range(1234,4988):
    for j in range(2,9):
        if isPandigitalMultiple(i,j):
            products.append(i * j)
            print(str(i) + " * " + str(j) + " = " + str(i * j))
print(sum(products))