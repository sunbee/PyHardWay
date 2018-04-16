import os

allPy = [x for x in os.listdir('.') if x.endswith("py")]
print "Got files as %r" % allPy

def runPy(pyFile):
    pyCommand = "python " + pyFile
    os.system(pyCommand)

pyTotal = len(allPy)
pyCount = 0
for ceFile in allPy:
    pyCount += 1
    print "Found files [%d/%d] as %s" % (pyCount, pyTotal, ceFile)
    runPy(ceFile)

print "Ran code using wrapper:"
runPy("chapter_01_ex2.py")

print "Ran code as string:"
os.system("python chapter_01_ex2.py")
