def f():
    global s
    print s
    s = "That's clear."
    print s


s = "Python is great!"
f()
print s


# https://www.python-course.eu/global_vs_local_variables.php


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0), "Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

# print KelvinToFahrenheit(273)
# print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5)

# https://www.tutorialspoint.com/python/assertions_in_python.htm

# http://www.pythonforbeginners.com/files/with-statement-in-python
# https://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
