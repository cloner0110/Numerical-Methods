import numpy as np
import matplotlib.pyplot as plt
grid=[10,20,50,100]
for gridres in range(len(grid)):
    nx=grid[gridres];ny=grid[gridres];lx=1;ly=1;dx=lx/nx;dy=ly/ny
    z=(dx/dy)**2;w=1.25;T=np.zeros((nx,ny),float);er=10
    xx=np.array([],float);yy=np.array([],float)
    k=0;res=np.array([],float)
    for i in range (0,nx):
        xx=np.append(xx,i*dx);yy=np.append(yy,i*dy)
    for i in range(0,len(T)):
        T[0,i]=1;T[ny-1,i]=1;Tn=np.copy(T)
    while er>=1e-5:
        for i in range (1,len(T)-1):
            for j in range (1,len(T)-1):
                Tn[i,j]=((-Tn[i-1,j]-z*Tn[i,j-1]-Tn[i+1,j]-z*Tn[i,j+1])/(-2*(1+z))-(1-w)*T[i,j])/w
        for j in range (1,len(T)-1):
            Tn[j,nx-1]=Tn[j,nx-2]
        er=abs(np.linalg.norm(Tn)-np.linalg.norm(T));res=np.append(res,er);T=np.copy(Tn);k=k+1
        if er>12:
            break
    plt.loglog(res,"-b")
    plt.xlabel('number of iteration - Gauss-seidell')
    plt.ylabel('Residual')
    plt.title('Convergence History')
    plt.legend(["Number of Iteration= {:3d} ".format(k)])
    plt.hold(False)
    plt.savefig("resgs {:3d} .png".format(grid[gridres]),format="png")

