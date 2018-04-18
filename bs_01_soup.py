from bs4 import BeautifulSoup

with open("tidy.html") as fp:
    soup2nuts = BeautifulSoup(fp, 'html.parser')

nuts = """
<span dir="ltr" class="selectable-text invisible-space copyable-text">" Failure is part of Success " -- is my life time slogan.
All attempts made in respect of Recharging,  in the form of digging trenches,  construction of ponds, connection to local streams from receiving end,  and to Open Wells in the supply or recharging end, were abandoned for the last 2 to 3 years.
Trenches made earlier to let water from open well  to the stream, when heavy rain fall years,  abandoned,  are going to be used in scanty rain fall years,  by constructing Check dams.</span>
"""
zuppe = BeautifulSoup(nuts)

# tag
tag = zuppe.span
print "Tag >>> Type is: %r" % type(tag)
print "Tag >>> Name is: %r" % tag.name
print "Tag >>> Attributes: class %r" % tag['class']

# Navigabe string
print "Tag >>> String: %r" % tag.string


# Use it!
blurb = soup2nuts.find("span", attrs={'class':'selectable-text invisible-space copyable-text'})
print type(blurb)
print blurb.string
fp.close()

"""
<span dir="ltr" class="selectable-text invisible-space copyable-text">From my 3 decades of cotton experience and 15 years of Bt Cotton experience,I can tell you that the Helicoverpa Armigra and Erias vitila haven't developed resistance as they are polyphogus. However PBW is an exclusive pest of cotton which has developed resistance against Bt Gene as farmers didn't take up refugiea of non By Cotton. If all the farmers collectively follow the PBW Control measures we can certainly tackle PBW menace.</span>
//*[@id="main"]/div[2]/div/div/div[3]/div[19]/div/div/div[2]/div[2]/span
#main > div._3zJZ2 > div > div > div._9tCEa > div:nth-child(19) > div > div > div._3Usvm.copyable-text > div._3zb-j.ZhF0n > span
<span dir="ltr" class="selectable-text invisible-space copyable-text">From my 3 decades of cotton experience and 15 years of Bt Cotton experience,I can tell you that the Helicoverpa Armigra and Erias vitila haven't developed resistance as they are polyphogus. However PBW is an exclusive pest of cotton which has developed resistance against Bt Gene as farmers didn't take up refugiea of non By Cotton. If all the farmers collectively follow the PBW Control measures we can certainly tackle PBW menace.</span>
"""
