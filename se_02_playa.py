import time
from selenium import webdriver

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://bandcamp.com/');
time.sleep(5) # Let the user actually see something!
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
