import numpy as np

# 1 
result=np.array([10,15,30,45,60])
#2
result=np.arange(5,15)
#3
result=np.arange(50,100,5)
#4
result=np.zeros(10)
#5
result=np.ones(10)
#6
result=np.linspace(0,100,5)
#7
result=np.random.randint(10,30,5)
#8
result=np.random.randn(10)
#9 yapamadım
result=np.random.randint(10,50,15).reshape(3,5)

print(result)