import math

# Get input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD/HCF
gcd = math.gcd(num1, num2)

# Display the GCD/HCF
print(f"The GCD/HCF of {num1} and {num2} is {gcd}")