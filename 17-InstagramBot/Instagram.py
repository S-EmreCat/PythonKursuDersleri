from instaUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self,username,password):
        ## chrome sayfasını ingilizce dili ile açıp ortak bir dil kontrolü sağlıyoruz
        self.browserProfile=webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser=webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        # giriş için username password bilgileri 
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        self.browser.maximize_window()
        time.sleep(3)
        
        usernameInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)
   
    def getFollowers(self,max):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
       
        # click işlemini aşağıdaki gibi değişkene atayarak da yapabiliriz
        # followers=self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        # followers.click()
       
        time.sleep(2)
        #önce div role=dialog olan etiketi alıp onun altında bulunan çok sayıda li olduğu için elements yazdık
        dialog=self.browser.find_element_by_css_selector("div[role=dialog] ul")
        
        # ilk takip listesine tıklanınca ilk 12 kişinin sayısını aldık
        followersCount=len(dialog.find_elements_by_css_selector("li"))
        print(f"first count:{followersCount} ")

        
        # takipçi listesini aşşağı ilerletmek için space tuşu ataması yapıyoruz
        # ama listede tuş özelliği olmadığı için listeye click yapıp sayfaya space tuşunu gönderiyoruz
        action=webdriver.ActionChains(self.browser)

        ## tüm takipci listesini istemez isek followerCount<max gibi bir tanımlama yapabilirz
        while followersCount < 30:
            ###   2 kere action yapıyorum çünkü tek seferde yapınca aşşağı kaydırmıyor
            dialog.click()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(1)
            newCount=len(dialog.find_elements_by_css_selector("li"))
            
            if followersCount != newCount:  
                followersCount=newCount
                print(f"update count: {newCount}")
                time.sleep(2)
            else:
                break
        ### takipci listesinin ekrana yazdırılması 
        followers=dialog.find_elements_by_css_selector("li")

### takipci listesini dosyaya yazdırıyoruz
        followerList=[]
        i=0
        for user in followers:
            i+=1
            if i==max:
                break
            link=user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)
        with open("followers.txt","w",encoding='utf-8') as file:
            for item in followerList:
                file.write(item+"\n")

    def followUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButon=self.browser.find_element_by_tag_name("button")
        
        if followButon.text=='Follow':
            followButon.click()
            time.sleep(2)
        else:
            print("Zaten Takiptesin")
        
    def unFollowUser(self,username):
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        allButons=self.browser.find_elements_by_css_selector("button span")
        time.sleep(2)
        for butons in allButons:
            # if etiketleri bu şekilde kontrol ediyoruz
            if butons.get_attribute('aria-label')=='Following':
                butons.click()
                time.sleep(1)
                ####   siteden xpath kopyalamayıp kendimiz yazdık 
                self.browser.find_element_by_xpath("//div[@class='mt3GC']//button[text()='Unfollow']").click()
            else:
                print("takip etmiyorsun")


instgrm=Instagram(username=username,password=password)
instgrm.signIn()
time.sleep(1)

instgrm.getFollowers(20)

# tekli kullanıcı için 
# instgrm.followUser("kod_evreni")

# çoklu kullanıcı için
# list=['kod_evreni',"kod.efendi"]
# for user in list:
#     instgrm.followUser(user)
#     time.sleep(3)

# instgrm.unFollowUser('kod_evreni')
