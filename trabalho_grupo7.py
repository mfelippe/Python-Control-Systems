#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as ctl

#função de Transferencia
# G(s) = 2.5/s^2+2s+5
num = np.array([2.5])
den = np.array([1,2,5])
G_s = ctl.tf(num,den)
print(G_s)

#resposta ao impulso
t = np.linspace (0,10,1000) #vetor de tempo
t1,y1 =ctl.step(G_s,t)
#plot da resposta ao impulso
plt.plot(y1,t1)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Resposta ao Impulso")
plt.grid()
plt.show()

#polos da tf
print("polos: ",ctl.pole(G_s))
# Zeros da tf
print("zeros: ",ctl.zero(G_s))
ctl.pzmap(G_s,title="Polos e zero da função de transferencia não compensada")
plt.show()

#Raizes da função de transferencia não Compensado
klist, rlist =ctl.rlocus(G_s,Plot=True,PrintGain=True,grid=False)
plt.title("LRG da função não compensada")
plt.grid()
plt.show()

#Obtendo parametros do sistema não compensado
#wn (frequencia natural não-amortecida)
wn = np.sqrt(float(num))
print("wn = ", wn)
#psi (coeficiente de amortecimento)
psi = 1/(2*wn)
print("psi = ",psi)
#ts (tempo de acomodação)
ts = 4/(psi*wn)
print('Ts = ',ts,'s')
#Mp (sobressinal)
mp = 100 * np.exp((-1*psi*np.pi)/np.sqrt(1-(psi*psi)))
print("MP = ",mp, "%")