from selenium import webdriver
import time
from selenium.webdriver.common.keys import keys
driver = webdriver.Chrome(r"C:\Users\chinnareddy\OneDrive\Desktop\chromedriver")
driver.maximize_window()
driver.get()
print(driver.current_url)
print(driver.current_window_handle)
driver.find_element_by_tag_name('a').click()
time.sleep(5)
print(driver.current_window_handle)
print(driver.window-handles)
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.find_element_by_name('q').send_keys('India',keys.ENTER)
time.sleep(5)
driver.execute_script('window.scrollTO(0,document.body.scrollHeight);')
time.sleep(5)
driver.find_element_by_xpath("//span[normalize_space()_'Next']").click()

