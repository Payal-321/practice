# Python script to save data to a specified file

def save_data_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
        print(f"Data has been successfully saved to '{file_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Get file name from user
    file_name = input("Please enter the file name (including .txt extension): ")
    # Get data from user
    data = input("Please enter the data you want to save: ")
    
    # Save data to the specified file
    save_data_to_file(file_name, data)

# Run the script
if __name__ == "__main__":
    main()
