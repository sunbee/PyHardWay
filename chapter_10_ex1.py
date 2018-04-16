tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
bell_cat = "\a"

print tabby_cat
print persian_cat
print backslash_cat
print bell_cat

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print fat_cat

slim_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print slim_cat

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
