from banking_system import Bank, Customer, Transaction

# Creating a bank
bank = Bank("My Bank")

# Adding customers
customer1 = Customer("Benson", "12345678", 1000)
customer2 = Customer("Jane", "87654321", 500)
bank.add_customer(customer1)
bank.add_customer(customer2)

# Displaying customers
bank.display_customers()

# Depositing money
transaction1 = Transaction("deposit", 200, customer1)
transaction1.process_transaction()

# Withdrawing money
transaction2 = Transaction("withdrawal", 300, customer2)
transaction2.process_transaction()

# Displaying account balance
customer1.display_balance()
customer2.display_balance()

# Removing a customer
bank.remove_customer(customer1)

# Displaying customers after removal
bank.display_customers()
