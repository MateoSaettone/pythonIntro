############################################
#                                          #
#            String manipulation           # 
#                                          #
#          Mateo Saettone Ascenzo          #
#                U56111212                 #
#                                          #
############################################

# Problem 1: Greeting Message
def greetingMessage():
    name = input("Enter your name: ")
    print(f"Hello, {name}! Nice to meet you.")

# Problem 2: Reversed String
def reversedString():
    word = input("Enter a word: ")
    print(f"Reversed: {word[::-1]}")

# Problem 3: String Length
def stringLength():
    sentence = input("Enter a sentence: ")
    print(f"The sentence has {len(sentence)} characters.")

# Problem 4: Vowel Count
def countVowels():
    input_string = input("Enter a word or sentence: ").lower()
    vowels = ['a', 'e', 'i', 'o', 'u']  
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:  
            vowel_count += 1
    
    print(f"Number of vowels: {vowel_count}")

# Problem 5: Palindrome Check
def palindromeCheck():
    word = input("Enter a word: ").lower()
    if word == word[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")

# Problem 6: Secret Message
def secretMessage():
    message = input("Enter your secret message: ")
    encrypted_message = message.upper()
    encrypted_message = message.upper().replace(" ", "_")
    print(f"Encrypted secret message: {encrypted_message}")

# Main function with a single run based on user's choice
def main():
    print("Menu:")
    print("1. Greeting Message")
    print("2. Reversed String")
    print("3. String Length")
    print("4. Vowel Count")
    print("5. Palindrome Check")
    print("6. Secret Message")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        greetingMessage()
    elif choice == "2":
        reversedString()
    elif choice == "3":
        stringLength()
    elif choice == "4":
        countVowels()
    elif choice == "5":
        palindromeCheck()
    elif choice == "6":
        secretMessage()
    
main()