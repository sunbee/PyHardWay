import time
from selenium import webdriver
from sys import exit

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://web.whatsapp.com/');
time.sleep(15) # Let the user actually see something!
sampleChat = driver.find_element_by_class_name('selectable-text')
print "Found %r" % sampleChat.text
driver.quit()

exit(0)

playPause = driver.find_element_by_class_name('playbutton')
playPause.click()
time.sleep(5) # Let the user actually see something!
playPause.click()
playables = driver.find_elements_by_class_name('discover-item')
print "Found %d playables like %s" % (len(playables), playables[3].find_element_by_class_name('item-title').text)
playables[3].find_element_by_class_name('item-link').click()
time.sleep(5) # Let the user actually see something!
for playable in playables:
    print "Now playing %s" % playable.find_element_by_class_name('item-title').text
    playable.find_element_by_class_name('item-link').click()
    time.sleep(5)
driver.quit()
