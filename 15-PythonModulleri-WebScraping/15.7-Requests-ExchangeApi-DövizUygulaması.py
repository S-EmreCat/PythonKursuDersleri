import requests
import json


api_url="https://api.exchangeratesapi.io/latest?base="

bozulan_doviz=input("Bozulan döviz türü:")
alınan_doviz=input("alınan döviz türü:")
miktar=int(input(f"ne kadar {bozulan_doviz} bozurmak istiyorsunuz?"))

result=requests.get(api_url+bozulan_doviz)  ## dövizz türünü belirlediğimiz parça

result=json.loads(result.text)

print("1 {0} = {1} {2} ".format(bozulan_doviz, result["rates"][alınan_doviz],alınan_doviz))
print("{0} {1} ={2}".format(miktar,bozulan_doviz,miktar*result["rates"][alınan_doviz]))
