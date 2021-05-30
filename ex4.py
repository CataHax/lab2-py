# Input books number, price

x = int(input("Enter the number of books:"))
y = float(input("Enter the book price:"))

# Compute the tax (7.5 percent of the total book price).

tax = 0.075

# Compute the shipping charge ($2 per book)

ship = 2
shipPerBook = x*2

# The price of the order is the sum of the total book price, the tax, and the shipping charge.

y = x*y
price = (y+shipPerBook)*tax

# Print the price of the order

print(price)
