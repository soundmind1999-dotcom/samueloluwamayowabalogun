account_balance = 0
transactions = []

def deposit(amount, account_balance, transactions):
    account_balance = account_balance + amount 
    record = f"Deposited: N{amount} | New balance: N{account_balance}"
    transactions.append(record)
    return account_balance


def withdraw(amount, account_balance, transactions):
    if amount > account_balance: 
           print("Withdrawal failed: insufficient funds") 
    else: 
        account_balance = account_balance - amount
        record = f"Withdrew: N{amount} | New balance: N{account_balance}"
        transactions.append(record)
    return account_balance



def show_transaction(transactions): 
    if not transactions: 
        print("No transaction yet.")
    else:
        print("\n Transactions so far: ")
        for t in transactions: 
            print(t)



print("Welcome to Transaction Log App!")

    app_menu = """
    Press 1: To Deposit
    Press 2: To Withdraw
    Press 3: To Show Transactions
    Press 4: To Exit
    """
print(app_menu)

app_option = int(input("Enter option: "))

match (app_option):
 
    case 1:
        print(f"Deposited N{amount} | New balance: N{account_balance}")
        amount = int(input("Enter deposit amount: "))
        account_balance = (amount, account_balance, transactions)


    case 2: 
       amount = int(input("Enter withdrawal amount: ")) 
       account_balance = withdraw(amount, account_balance, transactions)

    case 3: 
        show_transactions(transactions)

    case 4: 
        print (f"\n final balance: N{account_balance}")
        show_transactions(transactions)
        print("Thank you for using Transaction Log App!")



