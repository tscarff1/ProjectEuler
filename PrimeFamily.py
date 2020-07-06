#The algorithm:
# i = 56003
#while no solution is found:
#   i+=2 //We can ignore evens
#   if i is prime
#       replace each digit with the digits 0-9 and see if 8 of the possibilites are prime
#       replace every set of 2 digits with the same digit 0-9 and see if eight of the possibilities are prime
#       ... replace sets of digits until the set of digits would be the size of the number and see if eight of the possiblities are prime
import collections
primesFile = open("Primes", "r")
data = primesFile.readlines();
for line in data:
    primes = line.split()

def isPrime(num):
    sumDigits = 0
    for digit in str(num):
        sumDigits += int(digit)
    if sumDigits % 3 == 0:
        return False
    return str(num) in primes

def has_repeated_digits(num):
    #We don't care if the last digit is part of the repeated numbers since it can't be part of a prime family > 5 if the last digit is subbed
    #This is because 0,2,4,6,8 will all be even
    #We also don't care about the first digit, so I can ignore stuff like 00003
    substring = str(num)[1:-1]
    return len(set(substring)) < len(substring)

def get_all_perms(arrLen):
    perms = []
    if arrLen == 0:
        return []
    if arrLen == 1:
        return[0]
    if arrLen == 2:
        return [0,1]
    for i in range(2,arrLen):
        perms_with_size = get_perms_with_size(arrLen, i)
        if len(perms_with_size) > 0:
            perms.append(perms_with_size)
    return perms

def get_perms_with_size(arrLen, permLen):
    perms = []
    for i in range(1,arrLen - permLen+1):
        rec_perms([i],perms,permLen,i, arrLen)
    return perms


def rec_perms(prefix, perms, permLen, parentPos, arrLen):
    for i in range(parentPos + 1, arrLen - (permLen - len(prefix))):
        prefixCopy = prefix.copy()
        prefixCopy.append(i)
        if len(prefixCopy) == permLen:
            perms.append(prefixCopy)
        else:
            rec_perms(prefixCopy.copy(), perms, permLen, i, arrLen)

def getPrimeFamilySize(num, repeatedDigit):
    primeCount = 0
    for i in range(10):
        numStr = str(num)[0] + str(num)[1:-1].replace(repeatedDigit, str(i)) + str(num)[-1]
        if isPrime(int(numStr)):
            primeCount += 1
    return primeCount

def get_repeated_digits(num):
    substr = num[1:-1]
    repeated_digits = []
    digit_counts = collections.Counter(substr)
    for k in digit_counts:
        if digit_counts[k] > 1:
            repeated_digits.append(k)
    return repeated_digits


#define permutations list for numbers of each digit count
#NOTE: Not actually using all perms any more
perms = []
for i in range(10):
    perms.append(get_all_perms(i))

solutionFound = False

print(get_all_perms(6))

startInd = primes.index(("56003"))

for prime in primes[startInd:]:
    i = int(prime)
    if i > 56000 and has_repeated_digits(i):
        repeatedDigits = get_repeated_digits(prime)
        for d in repeatedDigits:
            if getPrimeFamilySize(i, d) > 7:
                print("FOUND:" + str(i) + ", " + str(repeatedDigits))

primesFile.close()