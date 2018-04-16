from sys import argv

script, source, target = argv

open(target, "w").write(open(source).read())
