threes = 3
fives = 5
sum = 0;
while threes < 1000:
    if threes % 5 != 0:
        sum += threes
    threes += 3

while fives < 1000:
    sum += fives;
    fives += 5;

print (sum)