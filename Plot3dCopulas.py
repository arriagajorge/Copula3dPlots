# import libraries and modify style
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-pastel')
#cmap = plt.get_cmap('coolwarm')
#plt.set_cmap(cmap)
import statsmodels.distributions.copula.api as cp

def CFD3d(cop, title, resl=50, savefig=False, cmap='coolwarm', shr=0.5, pltshow=True, fontsizeTitle=16, fontsizeAxis=14,
          xlabel='$u$', ylabel='$v$', zlabel='$C(u,v)$', figsize=(12,8), aspect=10):
    """ Plot the CDF of a copula in 3D 
    
    The copula is evaluated in a grid of points (u,v) in [0,1]x[0,1]
    
    Parameters
    ----------
    cop : statsmodels.distributions.copula.api.Copula
        Copula to plot.
    title : str
        Title of the plot.
    resl : int, optional
        Resolution of the plot, by default 50, which means 50x50 grid.
    savefig : bool, optional
        Save the figure, by default False.
    cmap : str, optional
        Color map to use, by default 'coolwarm'.
    shr : float, optional
        Shrink of the color bar, by default 0.5.
    pltshow : bool, optional
        Show the plot, by default True.
    fontsizeTitle : int, optional
        Font size of the title, by default 16.
    fontsizeAxis : int, optional
        Font size of the axis, by default 14.
    xlabel : str, optional
        Label of the x axis, by default '$u$'.
    ylabel : str, optional
        Label of the y axis, by default '$v$'.
    zlabel : str, optional
        Label of the z axis, by default '$C(u,v)$'.
    figsize : tuple, optional
        Size of the figure, by default (12,8).
    aspect : int, optional
        Aspect of the color bar, by default 10.
    
    Raises
    ----------
    NotImplementedError
        CDF not available in closed form. If the copula to plot is the Student t copula.
    
    Returns
    ----------
    plt : matplotlib.pyplot
        Plot of the CDF of the copula
        
    Examples
    ----------
    import statsmodels.distributions.copula as cp
    CFD3d(cp.GaussianCopula(corr=0.5), title="Cópula Gaussiana")
    CFD3d(cp.GaussianCopula(corr=0.5), title="Cópula Gaussiana", resl=75, figsave=True, pltshow=False)
    """
    Z = np.zeros((resl, resl), dtype=np.float64)
    for i,u in enumerate(np.linspace(0,1, num=resl)):
        for j,v in enumerate(np.linspace(0,1, num=resl)):
            Z[i,j] = cop.cdf([u,v])
    # Make a grid of points in [0,1]x[0,1]
    u = v = np.linspace(0, 1, resl)
    U, V = np.meshgrid(u, v)

    # Plot the surface.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(U, V, Z, cmap=cmap)
    fig.colorbar(surf, shrink=shr, aspect=aspect)
    ax.set_xlabel(xlabel, fontsize=fontsizeAxis)
    ax.set_ylabel(ylabel, fontsize=fontsizeAxis)
    ax.set_zlabel(zlabel, fontsize=fontsizeAxis)
    ax.set_title(title, fontsize=fontsizeTitle)
    #ax.set_zlim(0,10)
    #ax.view_init(elev=15, azim=90)
    
    if savefig:
        plt.savefig(title + "cfd.pdf", format='pdf')
    if pltshow:
        plt.show()
    return plt

def PDF3d(cop, title, resl=50, savefig=False, cmap='coolwarm', shr=0.5, pltshow=True, fontsizeTitle=16, fontsizeAxis=14,
          xlabel='$u$', ylabel='$v$', zlabel='$c(u,v)$', figsize=(12,8), aspect=10):
    """" Plot the PDF of a copula in 3D 
    
    The copula is evaluated in a grid of points (u,v) in [0,1]x[0,1]
    
    Parameters
    ----------
    cop : statsmodels.distributions.copula.api.Copula
        Copula to plot.
    title : str
        Title of the plot.
    resl : int, optional
        Resolution of the plot, by default 50, which means 50x50 grid.
    savefig : bool, optional
        Save the figure, by default False.
    cmap : str, optional
        Color map to use, by default 'coolwarm'.
    shr : float, optional
        Shrink of the color bar, by default 0.5.
    pltshow : bool, optional
        Show the plot, by default True.
    fontsizeTitle : int, optional
        Font size of the title, by default 16.
    fontsizeAxis : int, optional
        Font size of the axis, by default 14.
    xlabel : str, optional
        Label of the x axis, by default '$u$'.
    ylabel : str, optional
        Label of the y axis, by default '$v$'.
    zlabel : str, optional
        Label of the z axis, by default '$c(u,v)$'.
    figsize : tuple, optional
        Size of the figure, by default (12,8).
    aspect : int, optional
        Aspect of the color bar, by default 10.
    
    Returns
    ----------
    plt : matplotlib.pyplot
        Plot of the CDF of the copula
        
    Examples
    ----------
    import statsmodels.distributions.copula as cp
    PDF3d(cp.GaussianCopula(corr=0.5), title="Cópula Gaussiana")
    PDF3d(cp.GaussianCopula(corr=0.5), title="Cópula Gaussiana", resl=100, cmap='viridis', figsave=True, pltshow=False)
    """
    Z = np.zeros((resl, resl), dtype=np.float64)
    for i,u in enumerate(np.linspace(0,1, num=resl)):
        for j,v in enumerate(np.linspace(0,1, num=resl)):
            Z[i,j] = cop.pdf([u,v])
    # Make a grid of points in [0,1]x[0,1]
    u = v = np.linspace(0, 1, resl)
    U, V = np.meshgrid(u, v)

    # Plot the surface.
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(U, V, Z, cmap=cmap)
    fig.colorbar(surf, shrink=shr, aspect=10)
    ax.set_xlabel(xlabel, fontsize=fontsizeAxis)
    ax.set_ylabel(ylabel, fontsize=fontsizeAxis)
    ax.set_zlabel(zlabel, fontsize=fontsizeAxis)
    ax.set_title(title, fontsize=fontsizeTitle)
    #ax.set_zlim(0,10)
    #ax.view_init(elev=15, azim=90)
    
    if savefig:
        plt.savefig(title + "pdf.pdf", format='pdf')
    if pltshow:
        plt.show()
    return plt

#TODO add folders, and README