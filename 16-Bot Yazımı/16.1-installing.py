
"""
    pip install selenium 
    kodu ile terminal üzerinden selenium kurulumu yapılır.
    https://selenium-python.readthedocs.io/installation.html
    sitesi üzerinden çalışılmak istenilen driver indirilip python uygulaması ile aynı dizine atılır ya da path tanımı yapılır

"""

from selenium import webdriver

driver= webdriver.Chrome()  

url='http://sadikturan.com'   # açmak istediğimiz url girildi
driver.get(url)