##PRIME NUMBER CHECKER##

#collecting users input
num = float(input('input a number: '))

def is_prime(num):
    if num % 2 == 0 and num != 2:
        print(f'{num} is not a prime number')
    elif num % 3 == 0 and num != 3:
            print(f'{num} is not a prime number')    
    else:
        print(f'{num} is a prime number')

is_prime(num)

num = int(num)
def prime_checker(num):
    for i in range(2, num):
        is_prime
        if num % i ==0:
             not is_prime
    if is_prime:
         print('this is a prime number')
    else:
         print('not a prime number')  
prime_checker(num)