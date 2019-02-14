#!/usr/bin/python
# coding: utf-8

#Based on the code written by Jean-François Puget
#https://gist.github.com/jfpuget


import numpy as np
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors


@jit
#Mathematical definition of mandelbrodt set
def mandelbrot(z,maxiter,horizon,log_horizon):
    c = z
    for n in range(maxiter):
        az = abs(z)
        if az > horizon:
            return n - np.log(np.log(az))/np.log(2) + log_horizon
        z = z*z + c
    return 0


@jit
#Calculates the escape conditions for all pixels in the image
def mandelbrot_set(xmin,xmax,ymin,ymax,width,height,maxiter):
    horizon = 2.0 ** 40
    log_horizon = np.log(np.log(horizon))/np.log(2)
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = mandelbrot(r1[i] + 1j*r2[j],maxiter,horizon, log_horizon)
    return (r1,r2,n3)


#Saves the image with given filename
image_counter = 10
def save_image(fig):
    global image_counter
    filename = "mandelbrot_%d.png" % image_counter
    image_counter += 1
    fig.savefig(filename)



#Produces the computer image of the mandelbrodt set based on given conditions
def mandelbrot_image(xmin,xmax,ymin,ymax,width=5,height=5,maxiter=1000,cmap='jet',gamma=0.3):
    dpi = 1000
    img_width = dpi * width
    img_height = dpi * height
    x,y,z = mandelbrot_set(xmin,xmax,ymin,ymax,img_width,img_height,maxiter)
    
    fig, ax = plt.subplots(figsize=(width, height),dpi=72)
    ticks = np.arange(0,img_width,dpi)
    x_ticks = xmin + (xmax-xmin)*ticks/img_width
    plt.xticks(ticks, x_ticks)
    y_ticks = ymin + (ymax-ymin)*ticks/img_width
    plt.yticks(ticks, y_ticks)
    ax.set_title(cmap)
    
    norm = colors.PowerNorm(gamma)
    ax.imshow(z.T,cmap=cmap,origin='lower',norm=norm)  
    
    save_image(fig)



###Usage###



#mandelbrot_image(-2.0,0.5,-1.25,1.25,cmap='hot')

#x = np.linspace(-.8,-.75,.001)
#y = np.linspace(.02525,.0256,.000007)

#for i in range(0,50):
#	mandelbrot_image(x[i],{2},{3},{4},cmap='hot')


mandelbrot_image(-0.75125,-0.75105,.02525,.0256,cmap='jet')

#mandelbrot_image(-0.85,-0.8,0,0.05,cmap='hot')

#mandelbrot_image(-0.8,-0.75,0,0.05,cmap='hot')





















