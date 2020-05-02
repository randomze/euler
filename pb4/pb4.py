found = False

largest = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        number = i * j 
        
        number = [int(d) for d in str(number)]
        palindrome = True
        for k in range(len(number)//2 + 1):
            if number[k] != number[-(k + 1)]:
                palindrome = False
                break

        if palindrome == True:
            found = True
            number = int(''.join([str(i) for i in number]))
            if largest < number:
                largest = number
            break

print("biggest palindrome is {}".format(largest))
