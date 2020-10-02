import requests


class Github:
    def __init__(self):
        self.api_url='https://api.github.com'
        self.token='65ad1295935dffb9e933f2beb541f00d5174ee30'  ## kendi git adresimizde oluşturduğumuz token

    def getUser(self,username):
        response=requests.get(self.api_url+'/users/'+username)
        # json modülünü import etmeden response u json şekline çevirebiliriz
        return response.json()  
    def getRepositories(self,username):
        response=requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json()
    def createRepository(self,name): ## name dışında bilgilerde gönderebiliriz istersek
        response=requests.post(self.api_url+'/user/repos?access_token='+self.token,json={
        "name": name,
        "description": "This is your first repository",
        "homepage": "https://github.com/S-EmreCat",      ## kendi web sitemizin linki
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
        })
        return response.json()
github=Github()

while True:
    secim=input("1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nSeçim:")
    if secim=='4':
        break
    else:
        if secim=='1':
            username=input("username: ")
            result= github.getUser(username=username)
            print(f"name:{result['name']}\npublic repos: {result['public_repos']}\nfollowers: {result['followers']}\n ")
        elif secim=='2':
            username=input("username: ")
            result= github.getRepositories(username=username)   ### bize bir dizi döndüğü için elemanlara döngü ile ulaşacağız
            for repo in result:
                print(repo['name'])
        elif secim=='3':
            name=input("repository name: ")
            result=github.createRepository(name=name)
            print(result)
        else:
            print("yanlış seçim")
        
