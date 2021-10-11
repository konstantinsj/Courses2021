# 4. Prime numbers
#
# Find and output the first 20 (even better option to choose how many first primes we want) prime numbers in the form
# of a list i.e. [2,3,5,7,11, ...]
num = 1  # starting number
prime_list = []
list_count = 20  # length of the list

while len(prime_list) < list_count:
    num += 1
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        prime_list.append(num)

print(prime_list)
