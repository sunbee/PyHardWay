print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == '1':
    print "There is a giant bear eaiting a cheese cake. You:"
    print "1. Take the hot iron out of the fireplace and poke it right through the bear's eye."
    print "2. Cry for mama."

    bear = raw_input("> ")

    if bear == '1':
        print "Great! Now you made the bear mad! Good job!"
    elif bear == '2':
        print "Mama stopped caring after that Thanksgiving you spent with your girlfriend."
    else:
        print "Nice, you seized the bull by the horns. Unfortunately, this was a bear."

elif door == '2':
    print "You see an attacker armed with a banana. You:"
    print "1. Shoot the attacker. Then peel the banana and eat it."
    print "2. Counter with a pomegranate. After dropping a 1000 ton create on attacker's head."
    print "3. Avoid eye-contact and run."

    insanity = raw_input("> ")

    if insanity == '1' or insanity == '2':
        print "You are looking good! I wouldn't dare say otherwise to a man who killed someone for pointing a banana."
    else:
        print "Does your mama know she raised a wuss?"

else:
    print "You stumble around and fall on a knife and die. Good job!"
