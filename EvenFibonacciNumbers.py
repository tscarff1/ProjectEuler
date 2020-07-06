cur = 2;
prev = 1;
temp = 0;
sum = 0;
while cur < 4000000:
    if cur % 2 == 0:
        sum += cur
        print(cur)
    temp = cur;
    cur = temp + prev;
    prev = temp;
print("TOTAL")
print(sum)