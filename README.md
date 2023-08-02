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

cop.CFD3d(gc, title="Cópula Gaussiana")


cop.PDF3d(gc, title="Cópula Gaussiana")
```
![CFD Plot](https://drive.google.com/file/d/1L2f2HCvF6DUfX65cCJsdRss9UFPaGUKo/view?usp=sharing)
![PDF Plot](https://drive.google.com/file/d/1f0EGTKc5zpAmoN12dALj3EGyFTPDBg_F/view?usp=sharing)
