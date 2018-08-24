
# coding: utf-8

# In[57]:


# First, lets test the ability of Python to handle very large numbers.
# We can test this out by taking the factorial of, say, n=100
# Start with a smaller-sized problem, say, n=10
# Why are there zeros at the trailing end of the number?
# Hint! How many pairs in 1..n, when multiplied, yield 10?
# Ref: https://stackoverflow.com/questions/538551/handling-very-large-numbers-in-python
n=100

fact=1
for i in range(1, n-1):
    fact = fact*i
    
print "The factorial of %r is: %r" % (n, fact)
print "Adding 1 to this number, the result is: %r" % (fact+1)


# In[58]:


# The solution based on the common combinatorics problem as follows.
# How many ways that sum of x(i), where i range from 1 to m, total to s>
# Here, x(i) may not exceed r. That is, it is bounded by the range 0 to r.
# The first order of business is computing the binomial.

import unittest

def myFactorial(n):
    result = 1
    for i in range(0, n):
        result = result * (n-i)
    return result

class testMyFactorial(unittest.TestCase):
    
    def testMe_small(self):
        self.assertEqual(myFactorial(3), 6)
        self.assertEqual(myFactorial(4), 24)
        self.assertEqual(myFactorial(0), 1)
        
    def testMe_big(self):
        self.assertIsInstance(myFactorial(99), long)
        
suite = unittest.TestLoader().loadTestsFromTestCase(testMyFactorial)
unittest.TextTestRunner(verbosity=2).run(suite)

                         


# In[116]:


def myBinomial(x, m):
    result = 0
    if m < 0:
        result = 0
    else:
        result = 1
        for k in range(0, m):
            result = result * (x - k)
        result = result / myFactorial(m)
    return result
    
class testMyBinomial(unittest.TestCase):
    
    def testMe(self):
        self.assertEqual(myBinomial(2, 3), 0)
        self.assertEqual(myBinomial(3, 3), 1)
        self.assertEqual(myBinomial(5, 2), 10)
        self.assertEqual(myBinomial(5, -2), 0)

suite = unittest.TestLoader().loadTestsFromTestCase(testMyBinomial)
unittest.TextTestRunner(verbosity=2).run(suite)


# In[117]:


def myNb(s, r, m):
    result = 0
    if (s > 0 and r > 0 and m > 0):
        for k in range(0, int(s/r)+1):
            term = ((-1)**k) * myBinomial(m, k) * myBinomial(s+m-1-k*(r + 1), s-k*(r + 1))
            result = result + term
    
    return result

class testMyNb(unittest.TestCase):
    
    def testMe(self):
        self.assertEqual(myNb(24, 5, 5), 5)
        self.assertEqual(myNb(15, 4, 4), 4)
        self.assertEqual(myNb(14, 4, 4), 10)
        self.assertEqual(myNb(64, 22, 10), 72238591590L)
        
suite = unittest.TestLoader().loadTestsFromTestCase(testMyNb)
unittest.TextTestRunner(verbosity=2).run(suite)
        


# In[111]:



