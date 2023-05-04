import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-pastel')
cmap = plt.get_cmap('coolwarm')
plt.set_cmap(cmap)

import statsmodels.distributions.copula.api as cp

def CFD3d(cop, title, resl=50):
    Z = np.zeros((resl, resl), dtype=np.float64)
    for i,u in enumerate(np.linspace(0,1, num=resl)):
        for j,v in enumerate(np.linspace(0,1, num=resl)):
            Z[i,j] = cop.cdf([u,v])
    # Creamos una cuadrícula de puntos en el plano (u,v)
    u = v = np.linspace(0, 1, resl)
    U, V = np.meshgrid(u, v)

    # Graficamos la copula de min(u,v) usando plot_surface() y decoramos el gráfico
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(U, V, Z, cmap='coolwarm')
    fig.colorbar(surf, shrink=0.5, aspect=10)
    ax.set_xlabel('$u$', fontsize=14)
    ax.set_ylabel('$v$', fontsize=14)
    ax.set_zlabel('$C(u,v)$', fontsize=14)
    #ax.set_zlim(0,10)
    #ax.view_init(elev=15, azim=90)
    ax.set_title(title, fontsize=16)
    plt.savefig(title + "cfd.pdf", format='pdf')
    plt.show()
    return plt

def PDF3d(cop, title, resl=50):
    Z = np.zeros((resl, resl), dtype=np.float64)
    for i,u in enumerate(np.linspace(0,1, num=resl)):
        for j,v in enumerate(np.linspace(0,1, num=resl)):
            Z[i,j] = cop.pdf([u,v])
    # Creamos una cuadrícula de puntos en el plano (u,v)
    u = v = np.linspace(0, 1, resl)
    U, V = np.meshgrid(u, v)

    # Graficamos la copula de min(u,v) usando plot_surface() y decoramos el gráfico
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(U, V, Z, cmap='coolwarm')
    fig.colorbar(surf, shrink=0.5, aspect=10)
    ax.set_xlabel('$u$', fontsize=14)
    ax.set_ylabel('$v$', fontsize=14)
    ax.set_zlabel('$c(u,v)$', fontsize=14)
    #ax.set_zlim(0,10)
    #ax.view_init(elev=15, azim=90)
    ax.set_title(title, fontsize=16)
    plt.savefig(title + "pdf.pdf", format='pdf')
    plt.show()
    return plt
