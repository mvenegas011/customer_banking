# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    balance = float(input("Enter the initial balance of the Savings Account: "))
    interest_rate = float(input("Enter the interest rate: "))
    months = float(input("Enter the # of months for which interest is calculated: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Updated Savings Accoount Balance: ${updated_savings_balance:.2f}")
    print(f"Interest Earned: ${interest_earned:.2f}") 
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    balance = float(input("Enter the initial balance of the CD Account: "))
    interest_rate = float(input("Enter the CD interest rate: "))
    months = float(input("Enter the # of months for which interest is calculated: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(balance, interest_rate, months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"Updated CD Accoount Balance: ${updated_cd_balance:.2f}")
    print(f"Interest Earned: ${interest_earned:.2f}") 

if __name__ == "__main__":
    # Call the main function.
    main()
