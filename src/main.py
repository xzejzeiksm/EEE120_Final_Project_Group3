#Digital Password Lock System
#Python Software Prototype

STORED_PASSWORD="1011" #Correct password

def is_valid_password(password):
    #Checks if password has 4 bits and only 0 or 1
    if len(password) !=4:
        return False #Check if it's exactly 4 bits
    for bit in password:
        if bit not in "01":
            return False #Reject non-0/1 characters
    return True

def check_access(entered_password):
    #Checks if the entered password matches the stored password
    if entered_password==STORED_PASSWORD:
        return "Access Granted"
    else:
        return "Access Denied"

def run_tests():
    #Tests different password inputs
    print("\n--- Test Cases ---")

    test_passwords=["1011", "0000", "10A1", "101"]

    for password in test_passwords:
        if is_valid_password(password):
            result=check_access(password)
            print("Input:", password, "->", result)
        else:
            print("Input:", password, "-> Invalid password format")

def main(): #Shows the menu options
    while True:
        print("\n=== Digital Password Lock System ===")
        print("1. Enter password")
        print("2. Run test cases")
        print("3. Exit")

        choice=input("Choose an option: ").strip()

        if choice=="1":
            password=input("Enter a 4-bit password: ").strip()

            if is_valid_password(password):
                result=check_access(password)
                print("Status:", result)
            else:
                print("Status: Invalid input")
                print("Password must be exactly 4 bits, using only 0 or 1.")

        elif choice=="2":
            run_tests()

        elif choice=="3":
            print("Program ended.")
            break

        else:
            print("Invalid menu choice. Please try again.")

main()
