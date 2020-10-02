# etiketleri id,name,tag,class,css selector ile ulaşma
# https://selenium-python.readthedocs.io/locating-elements.html   kaynak link

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # enter girişi yapabilmek için import yapıyoruz

driver=webdriver.Chrome()
url="http://github.com"
driver.get(url)

#github sitesinde arama kısmına python yazdırıyoruz

# sitede sayfa kaynağından arama çubuğundan name="q" olduğunu buluyoruz
searchInput=driver.find_element_by_name("q")   
#searchInput=driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div/div/div/form/label/input[1]")  ## xpath ile ulaşma
time.sleep(1)
driver.maximize_window() # arama çubuğu küçük ekranda gözükmediği için büyütüyoruz
searchInput.send_keys("python")

time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result=driver.find_elements_by_css_selector(".repo-list-item a")  # repo-list-item class ının altındaki a etiketlerinin text bilgisini alıyoruz
for element in result:
    print(element.text)