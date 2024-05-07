import numpy as np
import matplotlib.pyplot as plt
import torch as th
from matplotlib import cm


def plot1D( fun, minx, maxx,stepf, stepquiver, clipq ):
    
    gf = th.func.grad(fun)
    x = np.arange(minx,maxx,stepf)

    y = fun(x)

    xx = np.arange(minx,maxx,stepquiver)
    x0,y0 = np.meshgrid(xx,0)
    v = 0
    u = np.array([ th.clip( gf( th.tensor(xi)),-clipq,clipq).numpy() for xi in xx ])

    plt.plot(x,y)

    plt.quiver(x0,y0,u,v)




def plot2D( fun, minx,maxx, miny,maxy,stepf,stepquiver ):
    XX = np.arange(minx, maxx, stepf)
    YY = np.arange(miny, maxy, stepf)
    X, Y = np.meshgrid(XX, YY)

    Z = fun( th.tensor(X),th.tensor(Y) ).numpy()

    XX2 = np.arange(minx, maxx, stepquiver)
    YY2 = np.arange(miny, maxy, stepquiver)
    gradg = th.func.grad(fun,(0,1))

    gg = [ gradg(th.tensor(xi),th.tensor(yi)) for yi in YY2 for xi in XX2 ]

    rshpgg = np.reshape( np.array( [ ( x.numpy(),y.numpy()) for x,y in gg]), (YY2.shape[0],XX2.shape[0],2))

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # Plot the surface.


    x, y, z = np.meshgrid(XX2,
                        YY2,
                        0)
    u = rshpgg[:,:,0:1]
    v = rshpgg[:,:,1:2]
    w = 0

    


    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False, alpha=0.5)
    ax.quiver(x,y,z,u,v,w, color = 'black')
    


def f( x ):
    return x**3 + 2*x**2 -x

plot1D(f,-3,3,0.1,0.5,4)

def g( x,y ):
    R = th.sqrt((0.75*x)**2+y**2 + 0.01)
    Z = th.sin(R)
    return Z

plot2D( g, -5,5.1,-5, 5.1 ,0.25,1.0)
plt.show()