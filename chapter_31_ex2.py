def exit_withPrompt():
    userPrompt =exitPrompt = "You stumble around and fall on a knife and die. Good job!"
    print "%s" % userPrompt

def beat_banana():
    userPrompt = """
    You entered the second doorself.
    You see an attacker armed with a banana. You:
    1. Shoot the attacker. Then peel the banana and eat it.
    2. Counter with a pomegranate. After dropping a 1000 ton create on attacker's head.
    3. Avoid eye-contact and run.
    Which one?
    """
    exitPrompt = "Does your mama know she raised a wuss?"
    retVal = {
        "1" : "You are looking good! I wouldn't dare say otherwise to a man who killed someone for pointing a banana.",
        "2" : "You are looking good! I wouldn't dare say otherwise to a man who killed someone for pointing a banana."
    }.get(raw_input(userPrompt), exitPrompt)
    print "%s" % retVal

def be_a_bear():
    userPrompt = """
    You entered the first door.
    There is a giant bear eaiting a cheese cake. You:
    1. Take the hot iron out of the fireplace and poke it right through the bear's eye.
    2. Cry for mama.
    Which one?
    """
    exitPrompt = "Nice, you seized the bull by the horns. Unfortunately, this was a bear."
    retval = {
        "1" : "Great! Now you made the bear mad! Good job!",
        "2" : "Mama stopped caring after that Thanksgiving you spent with your girlfriend."
    }.get(raw_input(userPrompt), exitPrompt)
    print "%s" % retval

def enter_door():
    userPrompt = "You enter a dark room with two doors. Do you go through door #1 or door #2? "
    {
        "1" : be_a_bear,
        "2" : beat_banana,
    }.get(raw_input(userPrompt), exit_withPrompt)()

enter_door()
