from sys import argv

script, user_name = argv
prompt = ">"

print "Hi %s, I am the %s script. Excuse the silliness of this set-up" % (
    user_name, script
)

print "I need to ask you a few questions."
print "Are you comfortable with me, %s?" % user_name

likes = raw_input(prompt)

print "Please tell me where you live, %s" % user_name
lives = raw_input(prompt)

print "Do you use a Windows PC or a Mac, %s" % user_name
pc = raw_input(prompt)

print '''
So you want us to believe that
someone who lives in %r and
says '%r' to a dumb terminal
owns a %r? Are you nuts?
''' % (lives, likes, pc)
