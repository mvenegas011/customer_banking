"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.    
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    #interest_rate = 0
    #Account = Account(balance,interest_rate)   
    interest_earned = balance * (interest_rate/100 * months/12)
    balance += interest_earned
    # Account.set_balance(balance)
    # Account.set_interest(interest_earned)
    return balance, interest_earned

    # def update_balance(self, interest_earned):
    # self.balance += interest_earned

# #####OK    
if __name__ == "__main__":
    create_savings_account()
    