/* Mini Project: Banking System  '''
   
'''Language used: python     
 Group Members: 1. Prasad Nikam (44) 
                2. Ramnath Tamangonda (49)
                3. Omkar Gaikwad (52)


class Account:
 def _init_(self, account_number, account_holder, balance=0):
 self.account_number = account_number
 self.account_holder = account_holder
 self.balance = balance
 def deposit(self, amount):
 if amount > 0:
 self.balance += amount
 print(f"Deposited: {amount}. New balance: {self.balance}")
 else:
 print("Deposit amount must be positive.")
 def withdraw(self, amount):
 if 0 < amount <= self.balance:
 self.balance -= amount
 print(f"Withdrawn: {amount}. New balance: {self.balance}")
 else:
 print("Invalid withdrawal amount.")
 def check_balance(self):
 return self.balance
class Bank:
 def _init_(self):
 self.accounts = {}
 def create_account(self, account_number, account_holder):
 if account_number not in self.accounts:
 self.accounts[account_number] = Account(account_number, account_holder)
 print(f"Account created for {account_holder} with account number {account_number}.")
 else:
 print("Account already exists.")
 def get_account(self, account_number):
 return self.accounts.get(account_number, None)
def main():
 bank = Bank()
 while True:
 print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Exit")
 choice = input("Choose an option: ")
 if choice == '1':
 acc_number = input("Enter account number: ")
 acc_holder = input("Enter account holder name: ")
 bank.create_account(acc_number, acc_holder)
 elif choice == '2':
 acc_number = input("Enter account number: ")
 account = bank.get_account(acc_number)
 if account:
 amount = float(input("Enter amount to deposit: "))
 account.deposit(amount)
 else:
 print("Account not found.")
 elif choice == '3':
 acc_number = input("Enter account number: ")
 account = bank.get_account(acc_number)
 if account:
 amount = float(input("Enter amount to withdraw: "))
 account.withdraw(amount)
 else:
 print("Account not found.")
 elif choice == '4':
 acc_number = input("Enter account number: ")
 account = bank.get_account(acc_number)
 if account:
 print(f"Current balance: {account.check_balance()}")
 else:
 print("Account not found.")
 elif choice == '5':
 print("Exiting...")
 break
 else:
 print("Invalid option. Please try again.")
if _name_ == "_main_":
 main()


/* Output

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 1
Enter account number: 1234
Enter account holder name: omkar
Account created for omkar. Account number: 1234

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 2
Enter account number: 1234
Enter amount to deposit: 1000
Deposited $1000.0. New balance: $1000.0

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 3
Enter account number: 1234
Enter amount to withdraw: 500
Withdrew $500.0. New balance: $500.0

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 4
Enter account number: 1234
Current balance: $500.0

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 5
Enter account number: 1234
Transaction History:
Deposited: $1000.0
Withdrew: $500.0

Welcome to the Banking System
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. Transaction History
6. Exit
Select an option (1-6): 6
Exiting the Banking System. Goodbye 
*/
