from math import *

class Euler():
    def __init__(self):
        print("\nwelcome to the euler project program")
        self.prime_number_list = []

    # problem 1
    def sum_of_multipliers_below(self, max):
        """
        max: max value that contains all mutipliers of 3 and 5
        return: sum of all mutipliers of 3 and 5 below max
        """
        multipliers = []
        n = 0
        while n < max:
            if n % 3 == 0 or n % 5 == 0:
                multipliers.append(n)
            n += 1
        return sum(multipliers)

    # problem 2
    def even_fibonacci_numbers(self, max):
        """
        max: max value that value list should obtain
        return: sum of even numbers of the fibonacci sequence below max
        """
        value = [1, 2]
        while value[-1] < max:
            value.append(value[-2]+value[-1])
        return sum([elt for elt in value if elt % 2 == 0])

    # problem 3
    def is_prime(self, x):
        """
        x = number to test if it is a prime number (divisible only by 1 and itself)
        return: True if x is a prime number, False if it isn't
        """
        if x >= 2:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
        return False
                

    def largest_prime_factor(self, number):
        """
        number: number on which is tested factors (prime or not)
        return: list of factors of number and the max factor of that list
        """
        factors = [1]
        for i in range(2, number//2+1):
            if number % i == 0:
                if self.is_prime(i):
                    factors.append(i)
        return max(factors), factors

    # problem 4
    def is_palindrome(self, x):
        """
        x: number to test if it is a palindrome
        return: True if x can be read in both directions, False if it can't
        """
        temp = x
        rev = 0
        while(x > 0):
            dig = x % 10
            rev = rev*10 + dig
            x = x//10
        return temp == rev

    def largest_palindrome_product(self, digits):
        """
        digits: number of digits desired to calculate the largest palindrome product in
        return: max palindromme of product of numbers from digits
        """
        nines = 0
        for i in range(0, digits):
            tens = 10**i
            nines = nines * 10 + 9
        maximum_palindrome = 0
        for i in range(tens, nines):
            for j in range(tens, nines):
                if self.is_palindrome(i*j) and (i*j) > maximum_palindrome:
                    maximum_palindrome = i*j
        return maximum_palindrome

    # problem 5
    def smallest_multiple(self, number):
        """
        number: range to test on the min number divisible by all numbers from that range
        return: min product divisible by all numbers from 1 to number
        """
        mult_list = []
        res = 1
        for i in range(1, number+1):
            current_number = i
            for elt in mult_list:
                if current_number % elt == 0:
                    current_number = int(current_number/elt)
            mult_list.append(current_number)
        for mult in mult_list:
            res *= mult
        return res

    # problem 6
    def sum_square_difference(self, max):
        """
        max: max number of the list ranging from 1 to max
        return: difference between the sum of the square of the range 1 to max, and the square of the sum of the range 1 to max 
        """
        square_sum_list = []
        sum_list = []
        for i in range(1, max+1):
            square_sum_list.append(i**2)
            sum_list.append(i)
        return abs(sum(square_sum_list) - sum(sum_list)**2)

    # problem 7
    def numberth_prime(self, number):
        """
        number: index of all the prime numbers
        return: the numberth prime number and its index, in this case number
        """
        i = 0
        n = 0
        while i < number:
            n += 1
            if self.is_prime(n):
                i += 1
        return n, i

    # problem 8
    def largest_product_in_serie(self, serie, length):
        """
        serie: list of numbers on which to calculate the maximum product in the range of nb_digits
        nb_digits: range of integers taken in serie to calculate its max product
        return: max product in range of nb_digits within serie
        """
        digit_number = [int(i) for i in str(serie)]
        max = 0
        for i in range(len(digit_number)-length+1):
            product = 1
            for j in range(length):
                product *= digit_number[i+j]
            if product > max:
                max = product
        return max

    # problem 9
    def special_pythagorean_triplet(self, number):
        """
        number: number on which is tested if a + b + c = number using pythagore theorem
        return: product of a, b, and c
        """
        for i in range(1,number):
            for j in range(1,number):
                if (i + j + sqrt(i**2 + j**2)) == number:
                    return int(i * j * sqrt(i**2 + j**2))

    # probem 10
    def sieve_of_eratosthenes(self, n):
        """
        n: number to list all prime numbers below
        return: sum of prime numbers below n
        """
        prime = [True for i in range(n + 1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p ** 2, n + 1, p):
                    prime[i] = False
            p += 1
        prime[0]= False
        prime[1]= False
        return sum([p for p in range(n + 1) if prime[p]])
    
    def summation_of_primes(self, max):
        """
        max: number to list all prime numbers below
        return: sum of prime numbers below max
        """
        return sum([i for i in range(max) if self.is_prime(i)])

    # problem 11
    def largest_product_in_grid(self, grid):
        # my code which didn't work for the diagonals, so after spending a few day on it, i gave up and used lucas willems' way
        """number_list = [int(i) for i in grid.split()]
        max = 0
        if direction == "horizontal":
            for i in range(len(number_list) - length + 1):
                product = 1
                for j in range(length):
                    product *= number_list[i+j]
                    if product > max:
                        max = product
        elif direction == "vertical" and length <= sqrt(len(number_list)):
            for i in range(len(number_list) - int(sqrt(len(number_list))*(length-1))):
                product = 1
                for j in range(length):
                    product *= number_list[i + j*length]
                    if product > max:
                        max = product
        elif direction == "diagonaldown" and length <= sqrt(len(number_list)):
            for i in range((int(sqrt(len(number_list)))+ 1 - length)**2):
                product = 1
                for j in range(length):
                    if i > int(sqrt(len(number_list))) - length and int(sqrt(len(number_list))) % i-1 == 0:
                        i += length
                    product *= number_list[i + (j*(int(sqrt(len(number_list)))+1))]
                    if product > max:
                        max = product
        elif direction == "diagonalup" and length <= sqrt(len(number_list)):
            for i in range((int(sqrt(len(number_list)))+ 1 - length)**2):
                product = 1
                for j in range(length):
                    if i > sqrt(len(number_list) - length):
                        i += length
                    print(number_list[i + (j*(length-1)+length-1)])
                    product *= number_list[i + (j*(length-1)+length-1)]
                    if product > max:
                        max = product
        return max"""

        number_list = [int(i) for i in grid.split()]
        product = []
        for i in range(400):
            if i%20 < 17:
                product.append(number_list[i]*number_list[i+1]*number_list[i+2]*number_list[i+3])
            if i < 340:
                product.append(number_list[i]*number_list[i+20]*number_list[i+40]*number_list[i+60])
            if i%20 < 17 and i < 340:
                product.append(number_list[i]*number_list[i+21]*number_list[i+42]*number_list[i+63])
            if i%20 > 3 and i < 340:
                product.append(number_list[i]*number_list[i+19]*number_list[i+38]*number_list[i+57])
        return max(product)

    # problem 12
    def highly_divisible_triangular_number(self, divisors_number):
        triangle_numbers_list = [1]
        adding = 1
        while len([i for i in range(1, triangle_numbers_list[-1]+1) if triangle_numbers_list[-1] % i == 0]) <= divisors_number:
            adding += 1
            triangle_numbers_list.append((triangle_numbers_list[-1]+adding))
        return triangle_numbers_list

    def test_function(self):
        print("\nwelcome to the test function")
        print(self.highly_divisible_triangular_number(2))


euler = Euler()
euler.test_function()