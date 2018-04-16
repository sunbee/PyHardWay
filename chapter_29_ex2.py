people = 20
cats =  30
dogs = 15

if people < cats:
    print "Too many cats! Cull 'em!"

if people > cats:
    print "The world is a bring place. Breed 'em!"

if people < dogs:
    print "There's drool all over. Neuter the punks."

if people > dogs:
    print "Break out beer. Why not?"

dogs += 5

if people >= dogs:
    print "We don't take kindly to people!"

if people <= dogs:
    print "We don't take kindly to dogs!"

if people == dogs:
    print "We don't take kindly to dog-people!"

# Why does python not support case-switch statement?
# Hee's why:
def numbers_to_letters(Numero):
    return {
        "0": "Zero",
        "1": "One",
        "2": "Two",
        "3": "Three"
    }.get(Numero, "Nothing")

Numero = raw_input("Give me a number between 0 and 3 to serialize: ")
print "Converted number %s to letter %s" % (Numero, numbers_to_letters(Numero))
print "Converted number %d to letter %s" % (1, numbers_to_letters(1))
