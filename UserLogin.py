# Define a base class for user-defined exceptions
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

# Define specific user-defined exceptions
class ValueTooSmallError(CustomError):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(CustomError):  
    """Raised when the input value is too large"""
    pass

# Main program to demonstrate the exceptions
def check_value(value):
    if value < 10:
        raise ValueTooSmallError("The value is too small!")
    elif value > 20:
        raise ValueTooLargeError("The value is too large!")
    else:
        print("The value is within the allowed range.")

try:
    # Take input from the user
    num = int(input("Enter a number: "))
    check_value(num)

except ValueTooSmallError as e:
    print(e)

except ValueTooLargeError as e:
    print(e)
