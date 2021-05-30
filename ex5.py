# Find at least three compile-time errors in the following program.

int x = 2 # no need for int
print(x, squared is, x * x) # "" these are missing in "squared is", squared is with double asteric **
xcubed = x *** 3 # remove one asteric

# the correct way

x = 2
print(x,"squared is", x**x)
xcubed = x**3
print(x,"cubed is", xcubed)
