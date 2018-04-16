from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_number, f):
    print line_number, f.readline()


handle = open(input_file)

print "Here's the contents of the secret file:\n"
print_all(handle)

print "Rewind after read, eh?"
rewind(handle)

print "Print two lines:\n"
print_line(1, handle)
print_line(2, handle)
