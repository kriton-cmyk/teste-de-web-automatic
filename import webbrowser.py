import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open Chrome
driver = webdriver.Chrome()

# Search for "stream" on Google
driver.get("https://www.google.com")
search_box = driver.find_element_by_name("q")
search_box.send_keys("stream")
search_box.send_keys(Keys.RETURN)

# Search for "deep rock galactic" on Google
time.sleep(2)  # wait for 2 seconds
search_box = driver.find_element_by_name("q")
search_box.clear()  # limpar o campo de busca
search_box.send_keys("deep rock galactic")
search_box.send_keys(Keys.RETURN)

# Open the game's page
time.sleep(2)  # wait for 2 seconds
game_page_link = driver.find_element_by_css_selector("div.g > div > div.rc > div.r > a")
game_page_link.click()