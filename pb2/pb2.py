fibonnaci = []
fibonnaci += [1]
fibonnaci += [2]

even_sum = 2
below_4million = True
index = 1

while below_4million:
    fibonnaci += [fibonnaci[index] + fibonnaci[index - 1]]
    index += 1
    if fibonnaci[index] > 4000000:
        below_4million = False
        break
    if fibonnaci[index] % 2 == 0:
        even_sum += fibonnaci[index]

print("the sum of the even elements of the fibonnaci sequence below 4 million is {}".format(even_sum))
