#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as ctl


# # trabalho 2 _ Sistema de Controle
# 

# In[2]:


# 1ºPasso - levantamento de requisito do sistema não compensado
#
#          função de Transferencia
# G(s) = 1/s(0.1s+1) => G(s) = 1/ 0.1s^2+ s

num = np.array([1])
den = np.array([0.1,1,0])
G_s = ctl.tf(num,den)
print(G_s)


# In[3]:


#bode do sistema não compensado

mag, phase, omega = ctl.bode(G_s)
plt.show()

# In[4]:


gm, pm, wg, wp = ctl.margin(G_s)
print('==================SISTEMA NÃO COMPENSADO====================')
#print('Margem de ganho:',gm)
print('Margem de fase:',pm)
#print('Frequencia para margem de ganho', wg)
print('Frequencia para margem de fase',wp)
#kv = limite s->0 s* G(s) = 1
kv = 1
print('kv = limite s->0 s* G(s) = ',kv)
print('=======================================================')


# In[5]:


# --------------------- requisito de novo Kv ------------
#                    NOVO_KV = limite s->0 s*G_s*kc
#                             20 = kc * 1
#                                 kc = 20 
#
#--------------------------------------------------------

kc = 20
kv = kc
kc_db = 20*np.log10(kc)
print('KC =',kc_db,"dB")


# In[15]:


#- 2º Passso - levantamento de dados do sistema utilizando Kc 
#
#                                  Diagrama de bloco do kc
#
#                imput -->()---|kc|--|G(s)|----->Output
#                         |                   |
#                         --------------------
#
G =kc_db*G_s
print(G)


# In[16]:


# bode do sistema compensado com  kc

mag, phase, omega = ctl.bode(G)
plt.show()

# In[17]:


gm, pm, wg, wp = ctl.margin(G)
print('========================================================')
#print('Margem de ganho:',gm)
print('Margem de fase:',pm)
#print('Frequencia para margem de ganho', wg)
print('Frequencia para margem de fase',wp)
#kv = limite s->0 s* G(s) = 20
kv = 20
print('kv = limite s->0 s* G(s) = ',kv)
print('=======================================================')


# In[18]:


#============= calculo para o compensador de avanço de fase ====================
#
#                  MF desejado é 65 graus e kc = 20
#
#=============================================================================

margem_de_erro = 3
phi_m = round(float(65 - pm + margem_de_erro),2)
print("PHI_m =",phi_m)

#calculo de a
a = (1-np.sin(np.deg2rad(phi_m)))/(1+np.sin(np.deg2rad(phi_m)))
print("a =",a)

#calculo de kc/√(a) /ganho do controlador na frequencia wn
#
#                                   kc
#              Gc_wm = |Gc(jw)| =   ------
#                                   √a
#
#-=========================================================
Gc_wm = round(-20* np.log10 (kc/np.sqrt(a)),2)
print("20 log(Kc/√a)=",Gc_wm)


# In[59]:


# ------------------- definindo de wn --------------------
#
#------------------------------------------------------

maglog = 20*np.log10(mag)

for i in range(0,np.size(mag)):                                   #percorre o vetor de mag gerado pela função bode                                               
    if  Gc_wm-1.1 <= maglog[i] < Gc_wm +1.2:                           #pega as wn entre os ganhos de  kc/√a +- 1                                                                     # salva os valores de omega no array t                                                                    
        wn = round(float(0.16 * omega[i]+8),2)
        print(wn)


# In[60]:


#================== Descobrindo T ===============================

T = round(1/(np.sqrt(a)*wn),2)
print(T)


# In[61]:


#============= Montando o compensador com base nos dados obtidos
#
#                              Ts + 1
#             C(s) = kc --------------------
#                             aTs + 1
#
#=================================================================
num = np.array([T,1])
den = np.array([a*T,1])
C_s = ctl.tf(kc*num,den)
print(C_s)
magc_s, phasec_s, omegac_s = ctl.bode(C_s)
plt.show()

# In[62]:


#====================== sistema compensad0 ======================
s_compensado = G_s * C_s
print(s_compensado)

magc, phasec, omegac = ctl.bode(s_compensado)
gmc, pmc, wgc, wpc = ctl.margin(s_compensado)
plt.show()

# In[64]:


print("MF =",round(pmc,2),"º")
print("kv =",kv)


# 

# In[14]:




