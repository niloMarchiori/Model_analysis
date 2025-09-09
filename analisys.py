import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_sub1(df_sub1):    
    # 1. Crie a figura e os eixos (axes) para 1 linha e 2 colunas de gráficos.
    # figsize ajusta o tamanho total da figura.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # --- Gráfico 1: F vs Kappa (no eixo ax1) ---
    F_array = np.array(df_sub1['F'].tolist())

    for i in range(F_array.shape[1]):
        ax1.plot(np.log10(df_sub1['kappa']), F_array[:, i], label=f'F[{i}] vs kappa')

    ax1.set_xlabel('log10(Kappa)')
    ax1.set_ylabel('F')
    ax1.set_title('F vs Kappa')
    ax1.legend()
    ax1.grid(True)

    # --- Gráfico 2: Tcmp vs Kappa (no eixo ax2) ---
    ax2.plot(np.log10(df_sub1['kappa']), df_sub1['Tcmp'], label='T vs Kappa', color='red')
    ax2.set_xlabel('log10(Kappa)')
    ax2.set_ylabel('Tcmp')
    ax2.set_title('Tcmp vs Kappa')
    ax2.legend()
    ax2.grid(True)

    # Ajusta o layout para evitar sobreposição de títulos e eixos
    plt.tight_layout()

    # Salva a figura em um arquivo
    plt.savefig('sub_1.png')

    # plt.show() # Descomente se estiver executando localmente e quiser exibir a figura


def plot_sub2(df_sub2):
    plt.figure(figsize=(10, 6))
    t_array = np.array(df_sub2['t'].tolist())  # shape: (len(kappa), n_ues)

    for i in range(t_array.shape[1]):
        plt.plot(np.log10(df_sub2['kappa']), t_array[:, i], label=f't[{i}] vs kappa')
    plt.xlabel('Kappa')
    plt.ylabel('t')
    plt.title('t vs Kappa')
    plt.legend()
    plt.grid()
    plt.figure(4, figsize=(10, 6))
    #Plot Tcom x log10(k)
    plt.plot(np.log10(df_sub2['kappa']), df_sub2['Tcom'], label='T vs Kappa')
    plt.xlabel('Kappa')
    plt.ylabel('Tcom')
    plt.title('Tcom vs Kappa')
    plt.legend()
    plt.grid()
    # Ajusta o layout para evitar sobreposição de títulos e eixos
    plt.tight_layout()

    # Salva a figura em um arquivo
    plt.savefig('sub_2.png')