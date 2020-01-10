def CreateMainMatrix(lx,ly,nx,ny):
    import numpy as np
    dx=lx/nx;dy=ly/ny;size=(nx)*(ny)
    Temperature=np.zeros(((nx),(ny)),float)
    temp_a=np.zeros(((size),(size)),float)
    temp_b=np.zeros((size),float)
    n=0
    for i in range (0,len(Temperature)):
        for j in range (0,len(Temperature)):
            if i==0: #top 
                if j==0:
                    temp_a[n,n+nx]=0;temp_a[n,n]=1;temp_a[n,n+1]=0;temp_b[n]=1
                    n=n+1
                elif 0<j<len(Temperature)-1:
                    temp_a[n,n+nx]=0 ;temp_a[n,n]=1;temp_a[n,n+1]=0;temp_a[n,n-1]=0;temp_b[n]=1
                    n=n+1
                else:
                    temp_a[n,n+nx]=0;temp_a[n,n]=1;temp_a[n,n-1]=0;temp_b[n]=1;n=n+1
            elif 0<i<len(Temperature)-1:
                if j==0: #left 
                    temp_a[n,n+nx]=0;temp_a[n,n-nx]=0;temp_a[n,n]=1;temp_a[n,n+1]=0;temp_b[n]=0;n=n+1
                elif 0<j<len(Temperature)-1: #internal Field
                    temp_a[n,n+1]=1;temp_a[n,(n-nx)]=(dx/dy)**2;temp_a[n,n]=-2*(1+((dx/dy)**2));temp_a[n,(n+nx)]=(dx/dy)**2;temp_a[(n),n-1]=1;temp_b[n]=0;n=n+1 
                else: #right 
                    temp_a[n,n+nx]=0;temp_a[n,n-nx]=0;temp_a[n,n]=-1;temp_a[n,n-1]=1;temp_b[n]=0;n=n+1
            else: #bottom 
                if j==0:
                    temp_a[n,n-nx]=0;temp_a[n,n]=1;temp_a[n,n+1]=0;temp_b[n]=1;n=n+1
                elif 0<j<len(Temperature)-1:
                    temp_a[n,n-nx]=0;temp_a[n,n]=1;temp_a[n,n+1]=0;temp_a[n,n-1]=0;temp_b[n]=1;n=n+1
                else:
                    temp_a[n,n-nx]=0;temp_a[n,n]=1 ;temp_a[n,n-1]=0;temp_b[n]=1;n=n+1
    return a,b