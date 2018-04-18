import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sys import exit

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
whatapp = driver.get('https://web.whatsapp.com/');
time.sleep(15) # Let the user actually see something!
# <span dir="auto" title="ProAgriSciencePanIndia" class="_1wjpf">ProAgriSciencePanIndia</span>
# <input type="text" class="jN-F5 copyable-text selectable-text" data-tab="2" dir="auto" title="Search or start new chat" value="">
searchStartChat = driver.find_element_by_xpath("//input[@title='Search or start new chat']")
print "Got search box as %r" % searchStartChat.get_attribute("title")
ActionChains(driver)\
    .move_to_element(searchStartChat)\
    .click(searchStartChat)\
    .send_keys('ProAgriSciencePanIndia')\
    .send_keys(Keys.ENTER)\
    .perform()

driver.quit()
exit(0)

handleBody = driver.find_element_by_tag_name('body')
for _ in range(3):
    handleBody.send_keys(Keys.HOME)
    sleep(7)
sampleChat = driver.find_element_by_class_name('copyable-text')
print "Found %r" % sampleChat.string



exit(0)
