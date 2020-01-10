import numpy as np
from CreateMainMatrix import CreateMainMatrix
import matplotlib.pyplot as plt
lx=1;ly=1;nx=10;ny=10;dx=lx/(nx-1);dy=ly/(ny-1)
tolerance=1e-5
z=CreateMainMatrix(lx,ly,nx,ny)
xx=np.array([],float)
yy=np.array([],float)
maxiteration=100
for i in range (0,nx):
    xx=np.append(xx,i*dx)
    yy=np.append(yy,i*dy) 
    a=z[0]
    b=z[1]
plt.figure(figsize=(15,15))
plt.spy(a)
plt.savefig('sparce.png',format="png")

