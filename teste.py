import constants as ctt
import numpy as np

np.random.seed(42)
#pos
d=np.random.uniform(*ctt.d_range,size=ctt.N)

#Com
# --- CORREÇÕES DE UNIDADE ---
# Converte a largura de banda B de MHz para Hz
B = ctt.B * 1e6
# Usa o valor de sigma para N0, que já está em Watts, conforme o artigo
N0 = ctt.sigma
# Converte o ganho do canal g0 de dB para escala linear
g0_linear = 10**(ctt.g0 / 10)
# Converte o tamanho do update 's' de KB para nats (conforme especificado no artigo)
# O artigo menciona s_n = 25,000 nats, que é ~4.5 KB
s_nats = 25000
# -------------------------

pmin=ctt.p_range[0]*np.ones(ctt.N)
pmax=ctt.p_range[1]*np.ones(ctt.N)

# Calcula h usando o g0 em escala linear
h=g0_linear*(ctt.d0/d)**4
# Define s como um array numpy em nats
s=s_nats*np.ones(ctt.N)


#Cmp
D=np.random.uniform(*ctt.D_range,size=ctt.N)*10**6  # Convert MB to bits
c=np.random.uniform(*ctt.c_range,size=ctt.N)
fmin=ctt.fmin*np.ones(ctt.N) * 10**9  # GHz to Hz
fmax=np.random.uniform(*ctt.fmax_range,size=ctt.N)*10**9  # GHz to Hz