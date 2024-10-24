import qrcode
import hashlib
import random

# Predefined users data: card number, username, hashed password, balance
users_data = {
    1234: {"username": "User1", "password": hashlib.sha256("pass1".encode()).hexdigest(), "balance": 1000},
    2345: {"username": "User2", "password": hashlib.sha256("pass2".encode()).hexdigest(), "balance": 5000},
    3456: {"username": "User3", "password": hashlib.sha256("pass3".encode()).hexdigest(), "balance": 3000},
    # Add up to 10 users in a similar format
}

# Function to authenticate card number and password
def authenticate_user(card_number, password):
    if card_number in users_data:
        hashed_input_password = hashlib.sha256(password.encode()).hexdigest()
        if users_data[card_number]["password"] == hashed_input_password:
            return True
    return False

# Function to generate a random MFA code
def generate_mfa_code():
    return random.randint(100000, 999999)

# Function to generate a QR code
def generate_qr_code(amount):
    qr_data = f"Transaction Amount: {amount}"
    qr_img = qrcode.make(qr_data)
    qr_img.save("transaction_qr.png")
    print("QR code for transaction generated: 'transaction_qr.png'")

# Main ATM function
def atm_interface():
    print("Insert your card:")
    card_number = int(input("Enter your card number: "))
    
    if card_number in users_data:
        password = input("Enter your password: ")
        
        # Authenticate the user
        if authenticate_user(card_number, password):
            print("Authentication successful!")
            
            # MFA Code
            mfa_code = generate_mfa_code()
            print(f"Your MFA code is: {mfa_code}")
            user_mfa_input = int(input("Enter the MFA code sent to your device: "))
            
            if user_mfa_input == mfa_code:
                while True:
                    print("\n1. Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Generate QR Code for Payment")
                    print("5. Exit")
                    choice = int(input("Enter your choice: "))
                    
                    if choice == 1:
                        # Check balance
                        print(f"Your balance is: {users_data[card_number]['balance']}")
                        
                    elif choice == 2:
                        # Deposit money
                        amount = int(input("Enter amount to deposit: "))
                        users_data[card_number]['balance'] += amount
                        print(f"Amount deposited successfully. New balance is: {users_data[card_number]['balance']}")
                        
                    elif choice == 3:
                        # Withdraw money
                        amount = int(input("Enter amount to withdraw: "))
                        if users_data[card_number]['balance'] >= amount:
                            users_data[card_number]['balance'] -= amount
                            print(f"Amount withdrawn successfully. New balance is: {users_data[card_number]['balance']}")
                        else:
                            print("Insufficient funds")
                            
                    elif choice == 4:
                        # Generate QR code for payment
                        amount = int(input("Enter the amount for QR code transaction: "))
                        generate_qr_code(amount)
                        print("Scan the QR code to complete your transaction using a mobile payment app.")
                        
                    elif choice == 5:
                        # Exit
                        print("Thank you for using the ATM!")
                        break
            else:
                print("MFA authentication failed!")
        else:
            print("Invalid password!")
    else:
        print("Invalid card number!")

# Run the ATM interface
atm_interface()
