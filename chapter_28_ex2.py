print("True and True evaluates to: %r") % (True and True)

codeBlock = """
True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
1 != 0 and 2 == 1
"test" != "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and not ("testing" == 1 or 1 == 0)
"chunky" == "bacon" and not (3 == 4 or 3 == 3)
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
"""

"""This\nThat""".split("\n")
codeBlock.split("\n")

for phrase in codeBlock.split("\n"):
    print("Processesing %r") % (phrase)
    if len(phrase) > 1:
        print("%r evaluates to: %r") % (phrase, eval(phrase))

count = 0
phrases = codeBlock.split("\n")
while True:
    if count == len(phrases):
        break
    phrase = phrases[count]
    count += 1
    if len(phrase) < 1:
        continue
    print "[%d] What does %s of length %d evaluate to?" % (count, phrase, len(phrase))
    yourAnswer = raw_input("Write True or False (or anything else to exit) ").lower()
    yourAnswer = {
        'true': True,
        'false': False
    }.get(yourAnswer,"Quit" )
    if yourAnswer == "Quit":
        break
    print "The answer is %r and you said %r" % (eval(phrase), yourAnswer)
print("Done!")
