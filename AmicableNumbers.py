import math

amNums = []
def sumOfDivisors(num):
    divList = []
    for x in range(1,int(math.sqrt(num))+1,1):
        if num % x == 0:
            divList.append(x)
            if num / x != x and x != 1:
                divList.append(num/x)
    return sum(divList)

for i in range(2, 10000):
    if i not in amNums:
        sumOfDivs = sumOfDivisors(i)
        if sumOfDivs != i:
            if sumOfDivisors(sumOfDivs) == i:
                amNums.append(i)
                if i != sumOfDivs:
                    amNums.append(sumOfDivs)

print(amNums)
print(sum(amNums))