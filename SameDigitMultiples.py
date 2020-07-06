import itertools
digits = ["123456", "741852","987654"]
perms = set()
for d in digits:
    perms.update([''.join(p) for p in itertools.permutations(d)])

print(perms)
for p in perms:
    i = int(p)
    #Check if i, 2i, 3i, 4i, 5i, and 6i all have the same digits
    mult = 2
    digitsMatch = True
    while mult < 7 and digitsMatch:

        iDigits = set(p)
        multDigits = set(str(i*mult))
        for x in multDigits:
            if x not in iDigits:
                digitsMatch = False
        mult += 1
    if digitsMatch:
        print(p)


