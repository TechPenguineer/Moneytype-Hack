from selenium import webdriver
from config.attributes import *

driver=webdriver.Chrome()
driver.get(webiste)
current_word_wrapper = driver.find_element_by_xpath('//*[@id="words"]/div[1]')