
# eccapsulation

# def outer(num1):
#     print("outer")
#     def inner_increment(num1):
#         print("inner")
#         return num1+1
#     num2=inner_increment(num1)
#     print(num2,num1)
# outer(10)

# def factorial(number):
#     if not isinstance(number,int):         ######    gönderilen değerin  o class a ait olmadığını kotrol eder.
#         raise TypeError("number most be an integer")
#     def inner_factorial(number):
#         if number==1:
#             return 1
#         return number*inner_factorial(number-1)
#     return inner_factorial(number)
# try:
#     print(factorial("a"))
# except Exception as ex:
#     print(ex)