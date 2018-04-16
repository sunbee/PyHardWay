people = 30
cars = 40
buses = 15

if cars > people:
    print "Affluenza has struck! More cars than people."
elif cars < people:
    print "We need car-pooling. Sharing is caring."
else:
    print "This is a dangerous tipping point in history. Whither from here?"

if buses > cars:
    print "Hurrah for public transport."
elif buses < cars:
    print "Have you tried taking the bus? It is relaxing!"
else:
    print "Separate lanes for buses and HOVs."

if people > buses:
    print "Be busy busin!"
else:
    print "OK"
