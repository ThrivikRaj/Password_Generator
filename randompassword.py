import random
import string
def generate_password(length, use_letters, use_numbers, use_symbols):
  
    character_set = ''
    
    if use_letters:
        character_set += string.ascii_letters  
    if use_numbers:
        character_set += string.digits 
    if use_symbols:
        character_set += string.punctuation  

    if not character_set:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password
def get_user_input():
 
    while True:
        try:
            length = int(input("Enter the desired password length (8-128): "))
            if length < 8 or length > 128:
                print("Password length must be between 8 and 128 characters.")
                continue
            
            use_letters = input("Include letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            
            return length, use_letters, use_numbers, use_symbols
        except ValueError:
            print("Invalid input. Please enter a number for the length.")
def main():
    print("Welcome to the Password Generator!")
    
    length, use_letters, use_numbers, use_symbols = get_user_input()
    
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()