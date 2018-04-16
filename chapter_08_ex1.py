formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 'Dumbledore')
print formatter % ("hun", "too", "tree", "fore")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
            "Gather ye rosebuds while ye may",
            "Olde time is still a-flying",
            "And this same flower that smiles today",
            "Tomorrow will be dying."
)
