from selenium import webdriver
import time
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.add_argument('--disable-software-rasterizer')
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\pythonSelenium\msedgedriver.exe") # 相应的浏览器的驱动位置
driver.maximize_window()
# driver.set_window_size(100%, 100%)
driver.get('http://localhost:8080/#/login')
driver.find_element_by_id('name').send_keys('haozexiang')#通过id定位
driver.find_element_by_id('password').send_keys('hzx123456')#通过id定位
driver.find_element_by_id('captcha').send_keys('1111')#通过id定位
driver.find_element_by_class_name('ant-btn-lg').click()#通过id定位
driver.implicitly_wait(4)
str1 = driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button/span')[0].get_attribute("innerHTML")
time.sleep(2)
if str1 == '知道了': driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button')[0].click()
# print(str1,'----------------')
time.sleep(2)
driver.quit()