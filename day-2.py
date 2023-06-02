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
