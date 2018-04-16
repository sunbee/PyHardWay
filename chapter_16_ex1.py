from sys import argv

script, filename = argv

print "We have orders to terminate %r." % filename
print "Do you care about %r?" % filename
raw_input("Enter Ctrl-C to show you care, otherwise hit Enter. Do it now.")

print "Your call. I am opening the file now..."
handle = open(filename, 'w')

print "Deleting the file contents. Ta-tah!"
handle.truncate()

print 'You can replace the contents with new tid-bits.'

tid = raw_input("tid: ")
bit = raw_input("bit: ")

handle.write(tid + "\n")
handle.write(bit)
handle.write("\n")

handle.close()
