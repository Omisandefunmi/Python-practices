# Let's write code that
# calculates the total bill at a restaurant,
# meal, plus tax, plus tip.
# We're going to prompt the user for the bill amount,
# the sales tax percentage,
# and the tip percentage,
# and then we'll print out that
# total bill amount in the format
# the total bill is and some dollar amount.
# Make sure you apply the tip after you add
# the tax amount and round
# the total bill amount to two decimal places.
# For example, let's say you went to
# a nice restaurant and ate a $30 meal.
# PA's sales tax is 6 percent,
# and you want to tip the waiter 18 percent.

bill = float(input('How much is your bill? '))
tax = float(input('what is the tax(%)? '))
tip_ = float(input('how much is the tip(%)? '))

tax_amount = (bill * tax) / 100
total_bill = bill + tax_amount
tip_amount = total_bill / 100
total_bill += round(tip_amount, 2)
print("The total bill is $", total_bill, sep='')
