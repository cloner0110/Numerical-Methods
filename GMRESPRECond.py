import scipy.sparse as spl
import scipy.sparse.linalg as splinalg
import numpy as np
from CreateMainMatrix import CreateMainMatrix
import matplotlib.pyplot as plt
lx=1
ly=1 
grid=[10,20,50,100]
for gridres in range(len(grid)):
    nx=grid[gridres];ny=grid[gridres];dx=lx/(nx-1);dy=ly/(ny-1);tol=1e-5;z=CreateMainMatrix(lx,ly,nx,ny)
    xx=np.array([],float);yy=np.array([],float)
    maxiter=100
    for i in range (0,nx):
        xx=np.append(xx,i*dx);yy=np.append(yy,i*dy)
    a=z[0];b=z[1];a2=spl.csc_matrix(a);m2=splinalg.spilu(a2,fill_factor=10);m_x=lambda x: m2.solve(x)
    m=spl.linalg.LinearOperator((len(a),len(a)),m_x);x0=np.zeros(len(a),float)
    def counter(rk=None):
        counter.niter +=1
        counter.res=np.append(counter.res,rk) 
        print("# iter {:3d}, residual={} ".format(counter.niter,str(rk)))
    counter.niter=0;counter.res=np.array([],float)
    x=spl.linalg.gmres(a2,b,x0,M=m,tol=tol,callback=counter);x2=np.linalg.inv(a).dot(b);x=x2
    T=np.zeros((nx,ny),float);n=0
    for i in range (0,len(T)):
        for j in range (0,len(T)):
            T[i,j]=x[n];n=n+1
        res=counter.res;co=np.array([],float)
    for i in range (0,len(res)):
        co=np.append(co,i+1)
    plt.loglog(co,res,'-b')
    plt.xlabel('number of iteration')
    plt.ylabel('Residuals')
    plt.title('Convergence History diagram')
    plt.legend(["Number of Iteration= {:3d} ".format(counter.niter)])
    plt.hold(False)
    plt.savefig("Residual-GMRES with Fill Factor =1 {:3d} .png".format(grid[gridres]),format="png")