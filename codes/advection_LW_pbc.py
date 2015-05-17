from pylab import *

def advection_LW_pbc(m):
    """
    Solve u_t + au_x = 0  on [ax,bx] with periodic boundary conditions,
    using the Lax-Wendroff method with m interior points.
     
    Returns k, h, and the max-norm of the error.
    This routine can be embedded in a loop on m to test the accuracy.
     
    Adapted from  http://www.amath.washington.edu/~rjl/fdmbook/  (2007)
    """

    a = 2             # advection velocity

    clf()              # clear graphics

    ax = 0
    bx = 1
    tfinal = 1.                # final time

    h = (bx-ax)/float(m+1)     # h = delta x
    k = 0.4*h                  # time step
    nu = a*k/h                 # Courant number
    x = linspace(ax,bx,m+2)    # note x[0]=0 and x[m+1]=1
                               # With periodic BC's there are m+1 unknowns 
                               # u[1] up to u[m+1], i.e. u[1:m+2]
    I = array(range(1,m+2), dtype=int)   # indices of unknowns

    nsteps = int(round(tfinal / k))      # number of time steps
    #nplot = 20       # plot solution every nplot time steps
                      # (set nplot=2 to plot every 2 time steps, etc.)
    nplot = int(round(nsteps/10))  # plot 10 frames
    #nplot = nsteps  # only plot at final time


    if abs(k*nsteps - tfinal) > 1e-5:
       # The last step won't go exactly to tfinal.
       print 'WARNING *** k does not divide tfinal, k = %9.5e' % k
       end

    # initial conditions:
    tn = 0
    def eta(x):
        beta = 600.
        return exp(-beta*(x - 0.5)**2)

    def utrue(x,t):
        # true solution for comparison

        # For periodic BC's, we need the periodic extension of eta(x).
        # Map x-a*t back to unit interval and evaluate initial data at this
        # point:

        xat = mod(x - a*t, 1.)
        return eta(xat)

    u0 = eta(x)
    u = u0

    # periodic boundary conditions:
    u[0] = u[m+1]   # copy value from rightmost unknown to ghost cell on left
    u = hstack((u, u[1]))   # add one more ghost cell to right, len(u) = m+3

    # initial data on fine grid for plotting:
    xfine = linspace(ax,bx,1001)
    ufine = utrue(xfine,0)

    # plot initial data:
    plot(x,u0,'b.-', label='computed')
    plot(xfine,ufine,'r', label='true')
    axis([0,1,-.2,1.2])
    legend()
    title('Initial data at time = 0')

    ans = raw_input('Hit <return> to continue  ')

    # main time-stepping loop:

    for n in range(nsteps):
        tnp = tn + k   # = t_{n+1}
        
        # Lax-Wendroff:
        u[I] = u[I] - 0.5*nu*(u[I+1] - u[I-1]) + \
                      0.5*nu**2 * (u[I-1] - 2*u[I] + u[I+1])

        # periodic boundary conditions:
        u[0] = u[m+1]   # copy value from rightmost unknown to ghost cell on left
        u[m+2] = u[1]   # copy value from leftmost unknown to ghost cell on right

        # plot results at desired times:
        if mod(n+1,nplot)==0 or n==nsteps-1:
            uint = u[0:m+2]  # points on the interval (drop ghost cell on right)
            ufine = utrue(xfine,tnp)
            clf()
            plot(x,uint,'b.-', xfine,ufine,'r')
            axis([0,1,-.2,1.2])
            title('t = %9.5e  after %4i time steps with %5i grid points' \
                           % (tnp,n,m+1))
            error = max(abs(uint-utrue(x,tnp)))
            print 'at time t = %9.5e  max error =  %9.5e' % (tnp,error)
            if n<nsteps-1: 
                ans = raw_input('Hit <return> to continue  ')

        tn = tnp   # for next time step
    return h,k,error


