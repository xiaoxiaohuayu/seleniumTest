from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
options = EdgeOptions()
options.use_chromium = True
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" # 浏览器的位置
driver = Edge(options=options, executable_path=r"D:\pythonSelenium\msedgedriver.exe") # 相应的浏览器的驱动位置
driver.get('http://localhost:8080/#/login')