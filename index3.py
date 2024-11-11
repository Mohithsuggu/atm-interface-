import mysql.connector

# Connect to MySQL database
conne = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='BANK'
)

# Function to open a new bank account
def OpenAccount():
    acc_no = input("Enter Account Number: ")
    name = input("Enter Name: ")
    dob = input("Enter Date Of Birth: ")
    address = input("Enter Address: ")
    phn_no = input("Enter Phone Number: ")
    opening_amount = int(input("Enter Opening Amount: "))

    entries1 = (acc_no, name, dob, address, phn_no, opening_amount)
    entries2 = (acc_no, name, opening_amount)
    
    sql1 = "INSERT INTO account VALUES (%s, %s, %s, %s, %s, %s)"
    sql2 = "INSERT INTO amount VALUES (%s, %s, %s)"
    
    c = conne.cursor()
    c.execute(sql1, entries1)
    c.execute(sql2, entries2)
    conne.commit()
    print("Data Entered Successfully.")
    MainMenu()

# Function to deposit an amount
def DepositAmount():
    acc_no = input("Enter Account Number: ")
    amount = int(input("Enter Amount to Deposit: "))

    sql = "UPDATE amount SET balance = balance + %s WHERE acc_no = %s"
    entries = (amount, acc_no)
    
    c = conne.cursor()
    c.execute(sql, entries)
    conne.commit()
    print("Amount Deposited Successfully.")
    MainMenu()

# Function to withdraw an amount
def WithdrawAmount():
    amount = int(input("Enter Amount to Withdraw: "))
    acc_no = input("Enter Account Number: ")

    # Fetch the current balance
    sql = "SELECT balance FROM amount WHERE acc_no = %s"
    entry = (acc_no,)
    c = conne.cursor()
    c.execute(sql, entry)
    res = c.fetchone()
    
    if res and res[0] >= amount:  # Check if sufficient funds
        total_amount = res[0] - amount
        sql = "UPDATE amount SET balance = %s WHERE acc_no = %s"
        entries = (total_amount, acc_no)
        c.execute(sql, entries)
        conne.commit()
        print("Amount Withdrawn Successfully.")
    else:
        print("Insufficient funds or invalid account.")
    MainMenu()

# Function to check the balance
def Balance():
    acc_no = input("Enter Account Number: ")
    sql = "SELECT balance FROM amount WHERE acc_no = %s"
    entry = (acc_no,)
    
    c = conne.cursor()
    c.execute(sql, entry)
    res = c.fetchone()
    
    if res:
        print("Balance of Account Number:", acc_no, "is", res[0])
    else:
        print("Account not found.")
    MainMenu()

# Function to display account details
def DisplayAccountDetails():
    acc_no = input("Enter Account Number: ")
    sql = "SELECT * FROM account WHERE acc_no = %s"
    entry = (acc_no,)
    
    c = conne.cursor()
    c.execute(sql, entry)
    res = c.fetchone()
    
    if res:
        print("Account Details:")
        print("Account Number:", res[0])
        print("Name:", res[1])
        print("DOB:", res[2])
        print("Address:", res[3])
        print("Phone Number:", res[4])
        print("Opening Amount:", res[5])
    else:
        print("Account not found.")
    MainMenu()

# Main menu function
def MainMenu():
    print("""
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE
    """)
    choice = input("Choose an Option: ")
    
    if choice == "1":
        OpenAccount()
    elif choice == "2":
        DepositAmount()
    elif choice == "3":
        WithdrawAmount()
    elif choice == "4":
        Balance()
    elif choice == "5":
        DisplayAccountDetails()
    elif choice == "6":
        print("Thank you for using the Bank Management System.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        MainMenu()

# Run the main menu
MainMenu()
