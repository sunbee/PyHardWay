from math import floor, ceil

def cheese_and_crakcers(cheese_count, boxes_of_crackers):
    print "You have %d of cheese!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Right on!"

print "Pass args directly to function as follows:\n"
cheese_and_crakcers(15, 7)

print "Pass args as variables as follows:\n"
cheesy = 7
crackpot = 9
cheese_and_crakcers(cheesy, crackpot)

print "Pass args evaluated inline as follows:\n"
cheese_and_crakcers(floor(1.6), 7+9)
cheese_and_crakcers(ceil(1.6), 7+9)
