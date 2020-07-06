#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits in the number 100!


#first, get the factorial of 100. We can skip multiplying by 100 since it
product = 1
for i in range(2,100):
    mult = i
    product *= mult
s = str(product)
sum = 0
for digit in s:
    if digit.isnumeric():
        sum += int(digit)

print(sum)