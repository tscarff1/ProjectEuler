num1 = 1000
num2 = 999
found = False
pals = []
while not found and num1 > 99:
    num2 = 1000;
    num1 -= 1
    while num2 > 99 and not found:
        num2 -= 1;
        total = num1 * num2;
        if str(total) == str(total)[::-1]:
            pals.append(total)
            print(str(num1) + " * " + str(num2) + " = " + str(total))

print(max(pals))

