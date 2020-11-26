#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as ctl

#%%

#função de Transferencia
# G(s) = 1/s(0.1s+1) => G(s) = 1/ 0.1s^2+ s
num = np.array([1])
den = np.array([0.1,1,0])
G_s = ctl.tf(num,den)
print(G_s)

#%%

mag, phase, omega = ctl.bode(G_s)
plt.show()