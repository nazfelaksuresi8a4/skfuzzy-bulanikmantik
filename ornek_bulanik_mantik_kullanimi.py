import skfuzzy as skf 
import skfuzzy.membership as ms
import numpy as np
import matplotlib.pyplot as plt 

x_pedal = np.arange(0,101,1)
x_speed = np.arange(0,101,1)
x_brake = np.arange(0,101,1)

pedal_low = ms.trimf(x_pedal,[0,0,50])
pedal_med = ms.trimf(x_pedal,[0,50,100])
pedal_high = ms.trimf(x_pedal,[50,100,100])

speed_low = ms.trimf(x_pedal,[0,0,60])
speed_med = ms.trimf(x_pedal,[20,50,80])
speed_high = ms.trimf(x_pedal,[40,100,100])

brake_por = ms.trimf(x_brake,[0,0,100])
brake_strong = ms.trimf(x_brake,[0,100,100])

plt.title('Pedal basıncı')
plt.plot(x_pedal,pedal_high,c='b',label='Yüksek')
plt.plot(x_pedal,pedal_low,c='g',label='Düşük')
plt.plot(x_pedal,pedal_med,c='r',label='Orta')
plt.legend()
plt.show()

plt.title('Araç hızı')
plt.plot(x_speed,speed_high,c='b',label='Yüksek')
plt.plot(x_speed,speed_low,c='g',label='Düşük')
plt.plot(x_speed,speed_med,c='r',label='Orta')
plt.legend()
plt.show()

plt.title('Fren Basıncı')
plt.plot(x_brake,brake_por,c='g',label='Düşük')
plt.plot(x_brake,brake_strong,c='b',label='Yüksek')
plt.legend()

plt.show()
   
