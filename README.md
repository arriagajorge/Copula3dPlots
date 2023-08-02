Uso de Plot3dCopulas.py

```Python
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-pastel')
cmap = plt.get_cmap('coolwarm')
plt.set_cmap(cmap)

import statsmodels.distributions.copula.api as cp
import Plot3dCopulas as cop

# copula gaussina corr=0.5
gc = cp.GaussianCopula(corr=0.5)

#Plot3D CFD & PDF
cop.CFD3d(gc, title="Cópula Gaussiana")
```
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1L2f2HCvF6DUfX65cCJsdRss9UFPaGUKo" alt="CFD Plot">
</p>

```Python
cop.PDF3d(gc, title="Cópula Gaussiana")
```

<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1f0EGTKc5zpAmoN12dALj3EGyFTPDBg_F" alt="PDF Plot">
</p>


The functions are made in such a way that you can modify parameters e.g. resolution, cmap, fontsize, etc.

Issues:
CFD cannot be plotted from t-student copula.
