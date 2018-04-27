import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sys import exit

print "Starting up WhatsApp in Chrome."
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
whatapp = driver.get('https://web.whatsapp.com/');
time.sleep(15) # Let the user actually see something!
# <span dir="auto" title="ProAgriSciencePanIndia" class="_1wjpf">ProAgriSciencePanIndia</span>
# <input type="text" class="jN-F5 copyable-text selectable-text" data-tab="2" dir="auto" title="Search or start new chat" value="">
# <span dir="ltr" class="selectable-text invisible-space copyable-text">Conservatively, he has saved at least 5.5m litres of water till date.</span>
print "WhatsApp loaded. Navigating to your group."
searchStartChat = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
print "Got search box as %r" % searchStartChat.get_attribute("title")
ActionChains(driver)\
    .move_to_element(searchStartChat)\
    .click(searchStartChat)\
    .send_keys('ProAgriSciencePanIndia')\
    .send_keys(Keys.ENTER)\
    .perform()
time.sleep(15)

print "Group chat loaded. Paging up."
chatBubble = driver.find_element_by_xpath('//span[@class="selectable-text invisible-space copyable-text"]')
print "Someone said: %r" % chatBubble.text

driver.execute_script("window.scrollTo(0, Y)")

time.sleep(15)
driver.quit()
exit(0)

# NO GO # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

driver.execute_script("return arguments[0].scrollIntoView();", chatBubble)

groupChat = driver.find_element_by_xpath('//div[@id="main"]')
for _ in range(9):
    print "Sending PAGE_UP"
    groupChat.send_keys(Keys.PAGE_UP)
    time.sleep(3)

groupChat = driver.find_element_by_tag_name('body')
for _ in range(3):
    groupChat.send_keys(Keys.HOME)
    time.sleep(7)

sampleChat = driver.find_element_by_class_name('copyable-text')
print "Found %r" % sampleChat.string



exit(0)
