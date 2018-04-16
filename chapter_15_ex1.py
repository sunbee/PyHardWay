from sys import argv

script, filename = argv

txt = open(filename)

print "The contents of your file %s are %r" % (filename, txt.read())

filename = raw_input("You can also give me the file name here: ")

txt = open(filename)

print "The contents of your file %s are %r" % (filename, txt.read())
