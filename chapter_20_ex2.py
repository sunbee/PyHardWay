from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_line(line_number, f):
    print line_number, f.readline()

def lines_in_file(fname):
    count = len(open(fname).readlines())
    return count

handle = open(input_file)

print "Here's the contents of the secret file:\n"
print_all(handle)

print "Rewind after read, eh?"
rewind(handle)

print "This is how many lines are in the file: %r\n" % lines_in_file(input_file)

for line_no in range(0, lines_in_file(input_file)):
    print_line(line_no, handle)
rewind(handle)


print "Print two lines:\n"
print_line(1, handle)
print_line(2, handle)
