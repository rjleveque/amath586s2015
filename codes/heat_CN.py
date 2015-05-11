"""
heat_CN.py  

adapted to Python from heat_CN.m, found at:
    http://www.amath.washington.edu/~rjl/fdmbook/  (2007)

See:
    https://docs.scipy.org/doc/scipy/reference/sparse.html
    http://mathesaurus.sourceforge.net/matlab-numpy.html

"""

from pylab import *

def heat_CN(m):
    """
    
    
    Solve u_t = kappa * u_{xx} on [ax,bx] with Dirichlet boundary conditions,
    using the Crank-Nicolson method with m interior points.
    
    Returns k, h, and the max-norm of the error.
    This routine can be embedded in a loop on m to test the accuracy,
    perhaps with calls to error_table and/or error_loglog.
    
    """

    from scipy import sparse
    from scipy.sparse.linalg import spsolve
    
    clf()              
    clear_each_frame = False    # set to True to clf for each time frame

    ulimits = [-0.1, 1.1]  # for setting y-axis limits
    
    ax = 0
    bx = 1
    kappa = .02               # heat conduction coefficient:
    tfinal = 1                # final time
    
    h = (bx-ax)/float(m+1)    # h = delta x
    x = linspace(ax,bx,m+2)   # note x(1)=0 and x(m+2)=1
                               # u(1)=g0 and u(m+2)=g1 are known from BC's
    k = 4*h                   # time step
    
    nsteps = int(round(tfinal / k))    # number of time steps
    nplot = 1      # plot solution every nplot time steps
                     # (set nplot=2 to plot every 2 time steps, etc.)
    #nplot = nsteps  # only plot at final time
    
    if abs(k*nsteps - tfinal) > 1e-5:
       # The last step won't go exactly to tfinal.
       print 'WARNING *** k does not divide tfinal, k = %9.5e' % k
    
    
    # true solution for comparison:
    # For Gaussian initial conditions u(x,0) = exp(-beta * (x-0.4)^2)
    beta = 150
    utrue = lambda x,t: exp(-(x-0.4)**2 / (4*kappa*t + 1./beta)) \
                / sqrt(4*beta*kappa*t+1.) 
    
    # initial conditions:
    u0 = utrue(x,0)
    
    
    # Each time step we solve MOL system U' = AU + g using the Trapezoidal method
    
    # set up matrices:
    r = 0.5 * kappa* k/(h**2)
    em = ones(m)
    em1 = ones(m-1)
    A = sparse.diags([em1, -2*em, em1], [-1, 0, 1], shape=(m,m))
    A1 = sparse.eye(m) - r * A
    A2 = sparse.eye(m) + r * A
    
    
    # initial data on fine grid for plotting:
    xfine = linspace(ax,bx,1001)
    ufine = utrue(xfine,0)
    
    # initialize u and plot:
    tn = 0
    u = u0
    
    plot(x,u,'b.-',label='computed')
    plot(xfine,ufine,'r',label='true')
    legend()
    ylim(ulimits)
    title('Initial data at time = 0')
    
    ans = raw_input('Hit <return> to continue  ')
    
    
    # main time-stepping loop:
    
    for n in range(1,nsteps+1):
         tnp = tn + k   # = t_{n+1}
    
         # boundary values u(0,t) and u(1,t) at times tn and tnp:
    
         g0n = u[0]
         g1n = u[m+1]
         g0np = utrue(ax,tnp)
         g1np = utrue(bx,tnp)
    
         # compute right hand side for linear system:
         uint = u[1:m+1]   # interior points (unknowns)
         rhs = A2.dot(uint)   # sparse matrix-vector product A2 * uint
         # fix-up right hand side using BC's (i.e. add vector g to A2*uint)
         rhs[0] = rhs[0] + r*(g0n + g0np)
         rhs[m-1] = rhs[m-1] + r*(g1n + g1np)
    
         # solve linear system:
         uint = spsolve(A1,rhs)   # sparse solver
    
         # augment with boundary values:
         u = hstack([g0np, uint, g1np])
    
         # plot results at desired times:
         if mod(n,nplot)==0 or n==nsteps:
            ufine = utrue(xfine,tnp)
            if clear_each_frame:  clf()
            plot(x,u,'b.-',label='computed')
            plot(xfine,ufine,'r',label='true')
            if clear_each_frame:  legend()
            ylim(ulimits)
            title('t = %9.5e  after %4i time steps with %5i grid points' \
                           % (tnp,n,m+2))
            error = abs(u-utrue(x,tnp)).max()
            print 'at time t = %9.5e  max error =  %9.5e' % (tnp,error)
            if n<nsteps: 
                ans = raw_input('Hit <return> to continue  ')
    
         tn = tnp   # for next time step

    return h,k,error 
