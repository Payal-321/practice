def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

# Get input from the user
N = int(input("Enter the number of prime numbers to print: "))

# Print the first N prime numbers 
prime_numbers = print_n_primes(N)
print(f"The first {N} prime numbers are: {prime_numbers}")
