# Function to search for the word in the sentence
def search_word(sentence, word):
    # Convert both sentence and word to lowercase for case-insensitive search
    if word.lower() in sentence.lower():
        return True
    else:
        return False

# Main function
def main():
    # Get input from the user
    sentence = input("Please enter a sentence: ")
    word = input("Please enter the word to search for: ")

    # Search for the word in the sentence
    if search_word(sentence, word):
        print(f"The word '{word}' was found in the sentence.")
    else:
        print(f"The word '{word}' was NOT found in the sentence.")

# Run the script
if __name__ == "__main__":
    main()
