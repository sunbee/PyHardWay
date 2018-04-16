def add(a, b):
    print "%d + %d = ?" % (a, b)
    return a + b

def subtract(a, b):
    print "%d - %d = ?" % (a, b)
    return a - b

def multiply(a, b):
    print "%d * %d = ?" % (a, b)
    return a * b

def divide(a, b):
    print "%d / %d = ?" % (a, b)
    return a / b

print "Test Drive:"

print "Sum of your age (%d) and my age (%d) is (%d)." % (17, 31, add(17, 31))
print "Diferent between your age (%d) and my age (%d) is (%d)." % (30, 12, subtract(30, 12))
print "There are (%d) dozen loaves of bread in a (%d)." % (divide(100, 12), 100)
print "You bought (%d) dozen oranges which is (%d)." % (4, multiply(4, 12))

what = add(35, subtract(74, multiply(180, divide(50, 2))))
print "You got %d" % what
