class Bank:
    """A class representing a bank."""
    
    def __init__(self, name):
        """Initialize the bank with a name and an empty list of customers."""
        self.name = name
        self.customers = []
    
    def add_customer(self, customer):
        """Add a customer to the bank's list of customers."""
        self.customers.append(customer)
    
    def remove_customer(self, customer):
        """Remove a customer from the bank's list of customers."""
        self.customers.remove(customer)
    
    def display_customers(self):
        """Display the list of customers in the bank."""
        if not self.customers:
            print("No customers in the bank.")
        else:
            print("Customers in the bank:")
            for customer in self.customers:
                print(customer)
                print("---------")
class Customer:
    """A class representing a bank customer."""
    
    def __init__(self, name, account_number, account_balance=0):
        """Initialize the customer with a name, account number, and account balance."""
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance
    
    def deposit(self, amount):
        """Deposit money into the customer's account."""
        self.account_balance += amount
        print(f"Deposited {amount}$ into the account. New balance: {self.account_balance}$")
    
    def withdraw(self, amount):
        """Withdraw money from the customer's account."""
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew {amount}$ from the account. New balance: {self.account_balance}$")
        else:
            print("Insufficient funds.")
    
    def display_balance(self):
        """Display the customer's account balance."""
        print(f"Account balance: {self.account_balance}$")
    
    def __str__(self):
        """Return a string representation of the customer."""
        return f"Name: {self.name}\nAccount Number: {self.account_number}\nAccount Balance: {self.account_balance}$"
class Transaction:
    """A class representing a bank transaction."""
    
    def __init__(self, transaction_type, amount, customer):
        """Initialize the transaction with a type, amount, and customer."""
        self.transaction_type = transaction_type
        self.amount = amount
        self.customer = customer
    
    def process_transaction(self):
        """Process the transaction and update the customer's account balance."""
        if self.transaction_type == "deposit":
            self.customer.deposit(self.amount)
        elif self.transaction_type == "withdrawal":
            self.customer.withdraw(self.amount)