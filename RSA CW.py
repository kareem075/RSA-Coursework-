import random
import math
import time
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
# -------------------------------------------second function----------------------------------------------------------------
def extended_GCD(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def calculate_private_exponent(e, phi_n):
    phi_n = T
    gcd, x, y = extended_GCD(e, phi_n)
    return x % phi_n
 
d = calculate_private_exponent(e, T)
print(f"Private exponent (d) will be: {d}")
print ("public key =", (e,n)," Private key=",(d, n))

# Encryption
M = int(input("Enter a Message:- "))
C = (M ** e) % n
print (C)

# Decryption
cypher = int(input("Enter Cypher Text:- "))
Message = (cypher ** d) % n 
print (Message)

def brute_force_d(n, e):
    d = 2
    begin_time = time.perf_counter()
    while True:
        if d*e % T == 1:
            end_time = time.perf_counter()
            elapsed_time = end_time - begin_time
            return d,'and time taken to get D is', elapsed_time
           
        d += 1
d =  brute_force_d(n, e)

print(f"Found private exponent (d): {d}")