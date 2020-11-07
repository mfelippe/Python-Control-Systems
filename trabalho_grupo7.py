#bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import control.matlab as ctl


#função de Transferencia
# G(s) = 10/s(s+1)
num = np.array([10])
den = np.array([1,1,0])
G_s = ctl.tf(num,den)

#plote do diagrama de Bode do sistema não compensado
w, mag, phase = ctl.bode(G_s)
# verificacao de margens de ganho e fase do sistema nao compensado
# gm = margem de ganho, pm = margem de fase
# wg = Frequência para margem de ganho (no cruzamento de fase, fase = -180 graus)
# wp ( float ) - Frequência para margem de fase (no cruzamento de ganho, ganho = 1)

gm, pm, wg, wp = ctl.margin(G_s)
#erro na verificação de magens de ganhos e fase do sistema
