print("Let's calculate our monthly expenses! Enter all values in $USD.")

rent = float(input("This month's rent: "))

groceries = float(input("What you spent for groceries: "))

utilities = float(input("This month's utility bill total: "))

other = float(input("Money you spent on other things: "))

total = rent + groceries + utilities + other

print("Your total expenses this month come out to $" + str(total))