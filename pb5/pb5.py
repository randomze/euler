primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

i = 0
smallest = 1
while primes[i] <= 20:
    temp = primes[i]
    while temp * primes[i] <= 20:
        temp *= primes[i]

    smallest *= temp
    i += 1

print("the smallest number that is evenly divisible by every number from 1 to 20 is {}".format(smallest))
