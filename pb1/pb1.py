def arithmetic_progression_sum(initial, final, reason):
    number_steps = (final - initial) // reason
    return (number_steps * (number_steps + 1) * reason) // 2;

sum_below_1000 = 0
#Add all the sum of all the multiples of 3 and 5
sum_below_1000 += arithmetic_progression_sum(1, 1000, 3)
sum_below_1000 += arithmetic_progression_sum(1, 1000, 5)
#Since we add the multiples of 3 and 5 separately, we count
#the numbers which are multiple of 3 AND 5 twice, therefore
#we need to subtract to our sum the sum of the numbers which
#are multiple of both
sum_below_1000 -= arithmetic_progression_sum(1, 1000, 3*5)

print("the sum of all multiples of 3 and 5 below 1000 is {}".format(sum_below_1000))
