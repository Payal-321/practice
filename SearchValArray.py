# Function to search for a value in the array
def search_array(arr, value):
    return value in arr

# Get input from the user
user_input = input("Enter the array elements separated by spaces: ")
search_value = int(input("Enter the value to search for: "))

# Convert input string to a list of integers
array = list(map(int, user_input.split()))

# Search for the value in the array
found = search_array(array, search_value)

# Display the result
if found:
    print(f"The value {search_value} is present in the array.")
else:
    print(f"The value {search_value} is not present in the array.")
