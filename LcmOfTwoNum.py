# Function to compute GCD
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Function to compute LCM
def lcm(x, y):
    return abs(x * y) // gcd(x, y)

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM
result = lcm(num1, num2)

# Display the LCM
print(f"The LCM of {num1} and {num2} is {result}.")
