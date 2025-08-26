import inputs as inp
import constants as ctt
import numpy as np
import pandas as pd
from sub1 import solve_SUB1
from sub2 import solve_SUB2
from analisys import plot_sub1, plot_sub2

kappa_i=1E-5
kappa_f=1E1
d_kappa=np.linspace(kappa_i, kappa_f, num=1000)

sub1={'F': [], 'Tcmp': [], 'kappa': []}
sub2={'Tcom': [], 't': [], 'kappa': []}
for k in d_kappa:
    T_cmp, f = solve_SUB1(kappa=k)
    sub1['F'].append(f)
    sub1['Tcmp'].append(T_cmp)
    sub1['kappa'].append(k)

    Tcom, t = solve_SUB2(ctt.N, kappa=k, s=inp.s, B=ctt.B, N0=ctt.N0, h=inp.h, pmin=inp.pmin, pmax=inp.pmax)
    sub2['Tcom'].append(Tcom)
    sub2['t'].append(t)
    sub2['kappa'].append(k)
#Convert to DataFrame
df_sub1 = pd.DataFrame(sub1)
df_sub2 = pd.DataFrame(sub2)
print(df_sub1)
print(df_sub2)

#Plot the results
# plot_sub1(df_sub1)
plot_sub2(df_sub2)