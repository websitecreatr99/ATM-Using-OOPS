class Atm:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("PIN Changed")
        else:
            print("Not Valid")

    def __menu(self):

        user_input = input('''
        Hello How would you like to proceed?
        1. Enter 1 to create PIN
        2. Enter 2 to deposit 
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to Exit
        ''')

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.deposit()
        elif user_input == 3:
            self.withdraw()
        elif user_input == 4:
            self.check_balance()
        elif user_input == 5:
            print("BYE")

    def create_pin(self):
        self.__pin = input("Enter your PIN")
        print("PIN set Successfully")

        self.__menu()

    def deposit(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            amount = int(input("Enter the Amount"))
            self.__balance = self.__balance + amount
            print("Deposit Successful")
        else:
            print("Invalid PIN")

        self.__menu()

    def withdraw(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            amount = int(input("Enter the Amount"))
            if self.__balance < amount:
                print("Insufficient Balance")
            elif amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Operation Successful")
        else:
            print("Invalid PIN")

        self.__menu()

    def check_balance(self):
        temp = input("Enter your PIN")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("Invalid PIN")

        self.__menu()





