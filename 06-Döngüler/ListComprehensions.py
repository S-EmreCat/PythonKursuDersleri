# numbers=[]
# for x in range(10):
#     numbers.append(x)                           # 2 si de aynı sonucu veriyor 
# print(numbers)

# sayilar=[x for x in range(10)]                 # ama bu daha pratik gibi
# print(sayilar)

# sayilar3=[y**2 for y in range(20) ]  # sayıların karesi
# print(sayilar3)
# sayilar3=[y  for y in range(20) if y%3==0]   # 3e bölünen sayıların kendisi ile çarpımı
# print(sayilar3)

# yazi='Hello'
# liste=[]
# for letter in yazi:
#     liste.append(letter)
# print(liste)

# yazi2=[harf for harf in yazi]
# print(yazi2)

# years=[1997,1954,1999,2008]
# ages=[2020-year for year in years]
# print(ages)

# results=[x if x%2==0 else 'TEK' for x in range(1,10)]  # if i else ile sonuçlandırmazsan hata alırsın
# print(results)

# dizi=[]
# for x in range(3):
#     for y in range(3):
#         dizi.append((x,y))
# print(dizi)

# numbers=[
#     (x,y) for x in range(3) for y in range(3)
# ]
# print(numbers)