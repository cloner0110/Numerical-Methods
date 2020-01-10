import scipy.sparse.linalg as spl
import scipy.sparse as spls
import numpy as np
from CreateMainMatrix import CreateMainMatrix
import matplotlib.pyplot as plt
from matplotlib import ticker, cm
grid=[10,20,50,100]
for gridres in range(len(grid)):
    lx=1
    ly=1
    nx=grid[gridres]
    ny=grid[gridres]
    dx=lx/(nx-1)
    dy=ly/(ny-1)
    tol=1e-5
    z=CreateMainMatrix(lx,ly,nx,ny)
    xx=np.array([],float)
    yy=np.array([],float)
    maxiter=100
    for i in range (0,nx):
        xx=np.append(xx,i*dx)
        yy=np.append(yy,i*dy) 
    a=z[0]
    b=z[1]
    a2=spls.csr_matrix(a)
    x0=np.zeros(len(a),float)
    def counter(rk=None):
        counter.niter +=1
        counter.res=np.append(counter.res,rk)
        print("# iter {:3d}, residual={} ".format(counter.niter,str(rk)))
    counter.niter=0
    counter.res=np.array([],float)
    x=spl.gmres(a2,b,x0,tol=tol,callback=counter)
    x=x[0]
    T=np.zeros((nx,ny),float) 
    n=0
    for i in range (0,len(T)):
        for j in range (0,len(T)):
            T[i,j]=x[n]
            n=n+1
        res=counter.res
        co=np.array([],float)
    for i in range (0,len(res)):
        co=np.append(co,i+1)
    plt.figure(figsize=(13,10))
    '''
    plt.loglog(co,res,'-b')
    plt.xlabel('number of iterations - GMRES')
    plt.ylabel('Residuals')
    plt.title('Convergence History ')
    plt.legend(["Number of Iteration= {:3d} ".format(counter.niter)])
    plt.hold(False)
    plt.savefig("Residual-GMRES {:3d} .png".format(grid[gridres]),format="png")
    '''
    plt.contourf(xx,yy,T,cmap=cm.PuBu_r)
    plt.colorbar()
    plt.legend(["Temperature distribution for Grid {:3d}".format(gridres)])
    plt.savefig('contour for grid {:3d}.png'.format(gridres),format="png")
    