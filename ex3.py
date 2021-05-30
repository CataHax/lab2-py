
x = "Mississippi"


l = len(x)

# print(l)

# print(x[0:3], "...", x[8:11]) MY VERSION

ex1 = x[0:3]
ex2 = x[len(x)-3 : len(x)]
#print(ex1,"...",ex2)      ANOTHER VERSION

# THE BEST WAY
print("%s...%s" % (ex1,ex2))
