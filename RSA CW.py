import random
import math
def primes_in_range(x, y):
    prime_list = []
    for n in range(x, y):
        is_prime = True
        for num in range(2, n):
            if n % num == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)
    return prime_list

prime_list = primes_in_range(1, 100)

random_prime1 = random.choice(prime_list)
random_prime2 = random.choice(prime_list)

print(f"Random prime number 1: {random_prime1}")
print(f"Random prime number 2: {random_prime2}")


n = random_prime1*random_prime2
T = (random_prime1-1)*(random_prime2-1)
e = 17


def is_coprime(e, T):
    gcd = math.gcd(e, T)
    return gcd == 1

if is_coprime(e, T):
    print(f"{e} and {T} are coprime.")
else:
    print(f"{e} and {T} are not coprime.")

