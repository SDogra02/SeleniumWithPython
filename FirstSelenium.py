from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("C:\\Users\\qanav\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://www.google.com")
driver.get("https://dekalblibrary.org/locations/dunw")
PageTitle = driver.title
#assert "Dunwoody" in PageTitle
print(PageTitle)
driver.maximize_window()
