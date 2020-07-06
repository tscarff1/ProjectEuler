#Project Euler problem 6

squareOfSum = sum(range(1,101))**2

diff = squareOfSum
for x in range (1,101):
    diff -= x**2

print(diff)