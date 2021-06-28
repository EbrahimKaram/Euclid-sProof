import math
import numpy

list_of_primes = []
for num in range(2, 20):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        list_of_primes.append(num)
        # print(num)

for j in range(len(list_of_primes)):
    # print(j)
    print(list_of_primes[:j + 1])
    product = numpy.prod(list_of_primes[:j + 1], dtype=numpy.int64)
    print("The product is ", product)

    # is this number prime
    number_to_check = product + 1
    if all(number_to_check % i != 0 for i in range(2, int(math.sqrt(number_to_check)) + 1)):
        print("This number is a prime ", number_to_check)
    else:
        divisors = []
        # What to check to whihc number these numbers are divisble by
        
        for i in range(2, number_to_check):
            if (number_to_check % i == 0):
                divisors.append(i)
        print(number_to_check, " is divisble by", divisors)
