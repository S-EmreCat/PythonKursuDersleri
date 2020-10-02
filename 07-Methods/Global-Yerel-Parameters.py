# x='global x'
# def funct(): 
#     x='yerel x'   # burada tanımlama yapmazsak 2 kere global x basar
#     print(x)
# print(x)
# funct()

x=50
def test():
    global x     # fonksiyon içerisinde x i bu şekilde tanımlarsak dışarıdaki x e doğrudan etki eder
    print(f'x in değeri: {x}')
    x=100
    print(f'changed x to {x}')

test()
print(x)