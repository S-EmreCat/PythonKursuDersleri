from selenium import webdriver
import time



driver=webdriver.Chrome()

url="http://github.com"

driver.get(url)

time.sleep(2)
driver.maximize_window()  ## açılan pencereyi tam ekran yapar
print(driver.title) # sayfanın title yazısı terminale yazdırılır
driver.save_screenshot("github.com-homage.png")  # açılan sayfanın ekran fotoğrafını alıp png dosyası oluşturup klasöre ekler

url2="http://github.com/sadikturan"
driver.get(url2)          ###    sayfadan yönlendirme yapmak istersen 2. url tanımlar get ile açarız
print(driver.title)
if "sadikturan" in driver.title:    ####   gittiğimiz sayfanın doğruluğunu kontrol ettik
    driver.save_screenshot("github-sadikturan.png")
time.sleep(2)

driver.back()  ## önceki sayfaya dön
# driver.forward() ## ileri sayfaya git
time.sleep(2)
driver.close()