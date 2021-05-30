# input a phone number

x = int(input("Enter a phone number:"))

# Take the string consisting of the first three characters and surround it with "(" and ") ". This is the area code.

# Concatenate the area code, the string consisting of the next three characters, a hyphen, and the string consisting
# of the last four characters. This is the formatted number.

xstr = str(x)
l = len(xstr)

x1 = xstr[0:3]
x2 = xstr[3:6]
x3 = xstr[len(xstr)-4:len(xstr)]

print("(",x1,")",x2,"-",x3) # EITHER THIS WAY

print("(%s)%s-%s" % (x1,x2,x3)) # OR THIS WAY (PREFERABLY)
