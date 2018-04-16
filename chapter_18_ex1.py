def print_many(*args):
    first, second = args
    print "You have me inputs as %r and %r, what for?" % (first, second)

def print_doubles(first, second):
    print "You have me inputs as %r and %r, what for?" % (first, second)
    return first + second

def print_singles(uno):
    print "You have me an input as %r for some reason." % uno

def print_some():
    print "Guess your point is no args is OK."

print_many("Sub", "Bee")
print_doubles("Radhe", "Krishna")
print "Got %r" % print_doubles("Radhe", "Krishna")
print_singles("Obergruppenfuhrer")
print_some()
