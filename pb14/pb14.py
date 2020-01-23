def len_collatz(l, n, r):
    length = 1

    if n < r and l[n] != -1:
        length = l[n]
    else:
        if n == 1:
            length = 1
        elif n % 2 == 1:
            length = len_collatz(l, 3 * n + 1, r) + 1
        else:
            length = len_collatz(l, n // 2, r) + 1

    if n < r:
        l[n] = length
    return length

l = [-1 for x in range(1000000)]
l[1] = 1
max_length = 1
for n in range(1, 1000000):
    length = len_collatz(l, n, 1000000)
    if length > l[max_length]:
        max_length = n

print("the number for which the sequence is largest is {}".format(max_length))
