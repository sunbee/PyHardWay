from sys import exit

double = lambda x: x * 2
print double(4)

showing = lambda x: "Now showing " + x
print showing("first")

def display_it(x):
    return lambda : "Now showing " + x

x = "first of all"
print display_it(x)()
print display_it("Second of all")()
print display_it()()

exit(0)
