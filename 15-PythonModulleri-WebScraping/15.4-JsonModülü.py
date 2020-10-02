# person={
#     "name": "Ali",
#     "languages":["python","c#"]
# }
# result=person["name"]
# result=person["languages"]
# result=person["languages"][1]
# print(result)

import json

person_string='{"name": "Ali", "languages":["python","c#"]}'  # bu şekilde string olarak tanımlarsak json olur

# json string to Dict

# result=json.loads(person_string)
# print(result)
# print(result["name"])

# with open("person.json") as f:  # açtığımız json dosyasındaki bilgileri alıp ekrana yazdırdık
#     data=json.load(f)
#     print(data["name"])
# person_dict={"name": "Ali", "languages":["python","c#"]}

# result=json.dumps(person_dict)
# print(result) # artık ["name"] şeklinde ulaşamayız
# print(type(result))  # dict to json string

# with open("person_dict","r") as f:   ###   dict de ki bilgileri jsona yazdırma
  #  json.dump(person_dict,f)

# person_dict=json.loads(person_string)   ###   tek satırda çıktı istersek
# result=json.dumps(person_dict, indent=4,sort_keys=True)  ###  alt alta çıktı istersek 
# print(person_dict)
# print(result)