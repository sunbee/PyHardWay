print "Sharpen the saw."
print "You\'d need to know \'bout escapes with \\ that do \n and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "---------"
print poem
print "---------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_point = int(raw_input("Tell me your starting number for the secret recipe? "))

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." % (secret_formula(start_point))
