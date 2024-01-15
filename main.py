import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x=np.linspace(-2*np.pi,2*np.pi,60)
X,Y=np.meshgrid(x,x)
Q=np.log((X-2)**2+np.abs((Y-3)**3))
Zgood=np.sin(Q)
print(Zgood.shape)
#plt.imshow(Zgood,extent=[x[0],x[-1],x[0],x[-1]],origin="lower")
#select pixel to demolish
prop_bad_pixel=.95
num_elements=np.prod(Zgood.shape)


badpix_idx=np.random.rand(int(num_elements * prop_bad_pixel))*num_elements

badpix_idx=np.floor(badpix_idx).astype(int)

Z=Zgood.copy()
i,j=np.unravel_index(badpix_idx,Zgood.shape)

Z[i,j]=np.nan


#find a list of the bad pixels.
badidx_i,badidx_j=np.where(np.isnan(Z))
goodidx_i,goodidx_j=np.where(np.isfinite(Z))
#interpolation instance using grindata
Znewpix=interpolate.griddata((goodidx_i,goodidx_j),Z[goodidx_i,goodidx_j],(badidx_i,badidx_j))

Zinterp=Z.copy()
Zinterp[badidx_i,badidx_j]=Znewpix

#visual
fig,ax= plt.subplots(1,3,figsize=(15,6))
ax[0].imshow(Zgood)
ax[0].set_title("Original")

ax[1].imshow(Z)
ax[1].set_title("corrupted")
ax[2].imshow(Zinterp)
ax[2].set_title("Interpolated")
plt.show()










