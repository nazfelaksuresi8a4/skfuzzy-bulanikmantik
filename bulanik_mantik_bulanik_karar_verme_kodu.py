import skfuzzy as fuzz
import numpy as np
import  matplotlib.pyplot as plt

'''DİZİLER'''
cold_array = np.arange(0,11,1)
warm_array = np.arange(0,21,1)
hot_array = np.arange(0,55,10)

'''ÜYELİK FONKSİYONLARI'''
cold_temp = fuzz.trimf(cold_array,[0,5,10])
warm_temp = fuzz.trimf(warm_array,[5,20,30])
hot_temp = fuzz.trimf(hot_array,[30,40,55])

temp = 20

'''ÜYELİKLER'''
cold_membership = fuzz.interp_membership(cold_array,cold_temp,temp)
warm_membership = fuzz.interp_membership(warm_array,warm_temp,temp)
hot_membership = fuzz.interp_membership(hot_array,hot_temp,temp)

fig,ax = plt.subplots(1,1,figsize=(5,4))

ax.plot(cold_array,cold_temp,label='cold')
ax.plot(warm_array,warm_temp,label='warm')
ax.plot(hot_array,hot_temp,label='hot')
ax.legend()

print(cold_membership)
print(warm_membership)
print(hot_membership)


plt.grid(True)
plt.show()
