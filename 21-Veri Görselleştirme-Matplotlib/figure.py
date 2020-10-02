import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,9,20)
y=x**3
z=x**2

"""  ÖRNEK 1 
# aynı karede farklı değerlere sahip yerleşimleri farklı 2 grafik
figure=plt.figure()
axes_cube=figure.add_axes([0.1,0.1,0.8,0.8]) ## sol alt sağ üst şeklinde bırakılacak boşluk için konumlandırma
axes_cube.plot(x,y,'b')
axes_cube.set_xlabel("X Axis")
axes_cube.set_ylabel("Y Axis")
axes_cube.set_title("Cube")

axes_square=figure.add_axes([0.15,0.6,0.25,0.25])
axes_square.plot(x,z,'r')
axes_square.set_xlabel("X Axis")
axes_square.set_ylabel("Y Axis")
axes_square.set_title("Quadratic")
plt.legend()
 """
""" # ÖRNEK 2 
# aynı karede farklı değerlere sahip tek (x,y) değerlerine sahip 2 grafik
figure=plt.figure()
axes=figure.add_axes([0,0,1,1])
axes.plot(x,y,label='Cube')
axes.plot(x,z,label='Square')
axes.legend(loc=4) # 1-sağ üst  2-sol üst köşe 3-sol alt köşe 4-sağ alt köşe
 """

# örnek 3
fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(4,4)) # figure için boy ayarlarması 
axes[0].plot(x,y)
axes[0].set_title("Cube")
axes[1].plot(x,z)
axes[1].set_title("Square")
plt.legend()
plt.tight_layout()
fig.savefig('figure.png') # figure için kayıt alabiliriz (pdf gibi türlerde de kayıt edebiliriz)
plt.show()