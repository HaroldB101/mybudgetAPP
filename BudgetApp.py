


class Budget:

    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount

#methods
    def deposit(self):
        return 'Amount has been deposited'
    
    def check_balance(self):
        return 'Please see your balance'

    def withdraw(self):
        return 'Withdrawn successfully'

    def transfer(self):
        return 'Transfered succcessfully'

category_1 = Budget("Food", 5000)
category_2 = Budget("Clothing", 2000)
category_3 = Budget("Entertainment", 3000)


print('These are the available options')
print('1. Deposit')
print('2. CheckBalance')
print('3. Withdraw')
print('4. Transfer')

selectedOption = int(input('Select an option \n'))

if(selectedOption == 1):
    depositAmount = input("How much would you like to deposit? \n")
    print (category_1.deposit())

elif (selectedOption == 2):
    print (category_2.check_balance())

elif (selectedOption == 3):
    withdrawalAmount = input("How much would you like to withdraw? \n")
    print (category_1.withdraw())

elif (selectedOption == 4):
    transferAmount = input("How much would you like to transfer? \n")
    print (category_1.transfer())

else:
    print('Invalid option selected, please try again')

