import time
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(
    executable_path=r"C:\Users\tejas\Desktop\pytest_sample\Test\chromedriver.exe"
)
driver.get('https://www.facebook.com/')
time.sleep(3)
#the below line i have used xpath of the create button which will be covered in later class
driver.find_element_by_xpath('(//a[@role="button"])[2]').click()
time.sleep(5)
driver.find_element_by_name('firstname').send_keys('your name')
#in the above you can enter the input in select locator 
"""
For Selecting the dropdown
we need to use the select class which in  webdriver.support.select module
Select class takes one mandidate argument the dropdown html element return by the 
locator
By select class obj we choose the dropdown options
"""
#the select class object is saved in select_day
select_day = Select(driver.find_element_by_name("birthday_day"))

time.sleep(3)
#.options will return the list of option hmtl element
# print(select_day.options)
#option.text will return the text of that html option
# for option in select_day.options:
#     print(option.text)
# #to select the any option we have many function 
# # .select_by_index this function take one argument index of the option as int
# time.sleep(3)
# select_day.select_by_index(2)

# # <option value="5">5</option>
# # The above is the html option tag to select that option there is other function
# # .select_by_value it will take the key of the value attribute as string
# select_day.select_by_value("5")
# # <option value="12">12</option>
# #To select the option based on visible text we can use the function
# # .select_by_visible_text it will take one argument the visible text of that option as string.
# select_day.select_by_visible_text('12')

# select_day.deselect_all()
# select_day.deselect_by_index()
# select_day.deselect_by_value()
# select_day.deselect_by_visible_text()
#the above functions are used in deselect the selected option 
#These can be used in the same way that of select_by_value and other used
