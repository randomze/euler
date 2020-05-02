number = 600851475143

factors = []
prime = False

while not prime:
    last_factor = 2
    for i in range(last_factor, number + 1):
        if number % i == 0:
            last_factor = i
            factors += [i]
            number = number // i
            break

    if number == 1:
        prime = True

number = 600851475143
print("the largest prime factor of {} is {}".format(number, factors[-1]))
