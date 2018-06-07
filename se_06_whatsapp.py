import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from sys import exit

SLEEP_TIME = 5
print "Starting up WhatsApp in Chrome."
driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
whatapp = driver.get('https://web.whatsapp.com/');
time.sleep(SLEEP_TIME) # Let the user actually see something!
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
time.sleep(SLEEP_TIME)

print "Group chat loaded. Finding sample text."
chatBubble = driver.find_element_by_xpath('//span[@class="selectable-text invisible-space copyable-text"]')
print "Someone said: %r" % chatBubble.text
print "Sample text found and printed. Seeking top of page."
driver.execute_script("window.scrollTo(0, -1080)")
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print "Got height for scrolling as %r" % last_height
SCROLL_PAUSE_TIME = 1
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print "Got new/old heights for scrolling as %r/%r" % (new_height, last_height)
    if new_height == last_height:
        break
    last_height = new_height

print "Tried operating scroll bar. Clicking on text in chat window to page up."
chatBubble.click()
chatBubble.send_keys(Keys.PAGE_UP)
time.sleep(SCROLL_PAUSE_TIME)


time.sleep(SLEEP_TIME)
driver.quit()
exit(0)

# NO GO # driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

driver.execute_script("window.scrollTo(0, 1080)")

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
