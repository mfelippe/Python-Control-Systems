#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as ctl

#função de transferência
num = np.array([1])
den = np.array([1,10,-24])
#Transformada
GH = ctl.tf(num,den)

print(GH)
#polos da tf
print(ctl.pole(GH))
# Zeros da tf
print(ctl.zero(GH))
ctl.pzmap(GH,title="polos e zeros da função")
plt.show()

#root locus
klist, rlist =ctl.rlocus(GH,Plot=True,PrintGain=True,grid=False)
plt.show()