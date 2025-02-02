import random

class Account:
    def __init__(self, account_holder, account_type, credit_score, annual_income):
        if not isinstance(credit_score, int):
            raise ValueError("Credit score must be a whole number")
        if credit_score < 300 or credit_score > 850:
            raise ValueError("Credit score must be between 300 and 850")
            
        self.account_holder = account_holder.upper()
        self.account_type = account_type.lower()
        self.credit_score = credit_score
        self.annual_income = annual_income
        self.balance = 0

    def account_detail(self):
        print("----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Credit Score: {self.credit_score}")
        print(f"Annual Income: ${self.annual_income}")
        print(f"Account Number: {self.account_number}")
        print(f"Account Balance: ${self.balance:.2f}")

class Debit(Account):
    def __init__(self, account_holder, credit_score, annual_income):
        super().__init__(account_holder, "debit", credit_score, annual_income)
        self.account_number = random.randint(444400000000, 444499999999)

    def deposit(self, amount):
        self.balance += amount
        print(f"Current account balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient fund!")
            print(f"Your balance is ${self.balance:.2f} only.")
            print("Try with less amount than balance.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawal successful!")
            print(f"Current account balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Available balance: ${self.balance:.2f}")

class Credit(Account):
    def __init__(self, account_holder, credit_score, annual_income):
        super().__init__(account_holder, "credit", credit_score, annual_income)
        self.account_number = random.randint(555500000000, 555599999999)
        self.credit_limit = self.set_credit_limit()

    def set_credit_limit(self):
        if 580 <= self.credit_score <= 669 and self.annual_income >= 60000:
            return 1000
        elif 670 <= self.credit_score <= 739 and self.annual_income >= 80000:
            return 2000
        elif self.credit_score >= 740 and self.annual_income >= 100000:
            return 4000
        else:
            return 500

    def make_purchase(self, purchase_amount):
        if purchase_amount > (self.credit_limit - self.balance):
            print("Insufficient fund!")
            print(f"Your balance is ${self.balance:.2f} and your credit limit is ${self.credit_limit:.2f}.")
            print(f"Try ${self.credit_limit - self.balance:.2f} or less amount.")
        else:
            self.balance += purchase_amount
            print(f"${purchase_amount:.2f} purchase successful!")
            print(f"Current account balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        fee = amount * 0.05  # 5% withdrawal fee
        total_withdrawal = amount + fee
        if total_withdrawal > (self.credit_limit - self.balance):
            print("Insufficient fund!")
            print(f"Your balance is ${self.balance:.2f} and your credit limit is ${self.credit_limit:.2f}.")
            print("Please also consider 5% withdrawal fee that applies to the withdrawal amount.")
        else:
            self.balance += total_withdrawal
            print(f"${amount:.2f} withdrawal successful!")
            print(f"Current account balance: ${self.balance:.2f}")

    def pay_credit(self, payment_amount):
        self.balance -= payment_amount
        print(f"Current account balance: ${self.balance:.2f}")

    def check_balance(self):
        print(f"Account balance: ${self.balance:.2f}")

    def account_detail(self):
        super().account_detail()
        print(f"Credit Limit: ${self.credit_limit:.2f}")
        
def get_valid_credit_score():
    while True:
        try:
            credit_score = int(input("Enter your credit score: "))
            if 300 <= credit_score <= 850:
                return credit_score
            else:
                print("Invalid credit score. Score must be between 300 and 850.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            
def get_valid_annual_income():
    while True:
        try:
            annual_income = float(input("Enter your annual income: $"))
            if annual_income < 0:
                print("Annual income cannot be negative.")
            else:
                return annual_income
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def transaction_menu(account):
    while True:
        print("\n        TRANSACTION")
        print("    *********************")
        print("        Menu:")
        print("        1. Account Details")
        print("        2. Check Balance")
        print("        3. Deposit (for debit card only)")
        print("        4. Withdraw (for debit card only)")
        print("        5. Make a Purchase (for credit card only)")
        print("        6. Withdraw from Credit Card")
        print("        7. Make a Payment to Your Credit Card")
        print("        8. Exit")
        print("    *********************")

        choice = input("\nEnter 1, 2, 3, 4, 5, 6, 7, or 8: ")

        if choice == '1':
            account.account_detail()
        elif choice == '2':
            account.check_balance()
        elif choice == '3' and isinstance(account, Debit):
            amount = float(input("The amount you want to deposit into your debit card: $"))
            account.deposit(amount)
        elif choice == '4' and isinstance(account, Debit):
            amount = float(input("The amount you want to withdraw from your debit card: $"))
            account.withdraw(amount)
        elif choice == '5' and isinstance(account, Credit):
            amount = float(input("The amount to spend for a purchase from your credit card: $"))
            account.make_purchase(amount)
        elif choice == '6' and isinstance(account, Credit):
            amount = float(input("The amount you want to withdraw from your credit card: $"))
            account.withdraw(amount)
        elif choice == '7' and isinstance(account, Credit):
            amount = float(input("The amount you want to pay for the balance on your credit card: $"))
            account.pay_credit(amount)
        elif choice == '8':
            transaction_number = random.randint(10000, 1000000)
            print("\n            printing receipt..............")
            print("      ******************************************")
            print("          Transaction is now complete.")
            print(f"          Transaction number: {transaction_number}")
            print(f"          Account holder: {account.account_holder}")
            print(f"          Account number: {account.account_number}")
            print(f"          Account balance: ${account.balance:.2f}")
            print("\n          Thanks for choosing FINTECH as your bank!")
            print("      ******************************************")
            break
        else:
            print("Invalid choice or operation not allowed for this account type. Please try again.")

def main():
    print("*******WELCOME TO BANK OF FINTECH*******")
    print("___________________________________________________________")
    print("----------ACCOUNT CREATION----------")

    account_holder = input("Enter your name: ")
    account_type = input("Enter your account type: (Please type either credit or debit) ")
    
    try:
        credit_score = get_valid_credit_score()
        annual_income = get_valid_annual_income()

        if account_type.lower() == "debit":
            user_account = Debit(account_holder, credit_score, annual_income)
        elif account_type.lower() == "credit":
            user_account = Credit(account_holder, credit_score, annual_income)
        else:
            print("Invalid account type! Please enter either 'credit' or 'debit'.")
            return

        print("Congratulations! Account created successfully......")

        while True:
            transaction_decision = input("\nDo you want to do any transaction?(y/n): ").lower()
            if transaction_decision == 'y':
                transaction_menu(user_account)
            elif transaction_decision == 'n':
                print("Thank you for visiting!")
                break
            else:
                print("Please enter 'y' for Yes or 'n' for No.")
                
    except ValueError as e:
        print(f"Error: {e}")
        print("Account creation failed. Please try again.")

if __name__ == "__main__":
    main()

