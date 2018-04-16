from sys import argv
from os.path import exists

script, source, target = argv

print "Copying from %s to %s. Just like in the movies." % (source, target)
print "No animals were harmed in the Copying of these files."

if exists(target):
    print "The target file exists already and shall be overwritten."
else:
    print "Did you forget to check for missing file?"

handle_source = open(source)
handle_target = open(target, "w")

contents = handle_source.read()
handle_target.write(contents)

print "Task completed!"
print "Wrote %d bytes from  %s to %s" % (len(contents), source, target)
print "Time for a(nother) beer."

handle_source.close()
handle_target.close()
