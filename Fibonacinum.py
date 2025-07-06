# Function to generate Fibonacci series
def fibonacci_series(n):
    series = [0, 1]
    while len(series) < n:
        next_value = series[-1] + series[-2]
        series.append(next_value)
    return series[:n]

# Get input from the user
N = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate and print the Fibonacci series
fib_series = fibonacci_series(N)
print(f"The first {N} Fibonacci numbers are: {fib_series}")
