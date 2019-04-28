from argparse import ArgumentParser
from matplotlib import pyplot as plt
import numpy as np

class julia(object):
    '''
    Produces a graph of a Julia graph
    '''
    
    def __init__(self, x_axis_lim, y_axis_lim, resolution):
        self.x_dim = x_axis_lim
        self.y_dim = y_axis_lim
        self.resolution = resolution

    def generateData(self, A, x, y, resolution,zx,zy):
        stop = False
        while not stop:
            zx_squared = zx * zx
            zy_squared= zy * zy
            if zx_squared + zy_squared >= 4 or resolution <=1:
                stop = True
            zy = 2.0 * zx * zy + 0.27015
            zx = zx_squared - zy_squared - 0.7
            resolution -= 1
        A[y][x]=resolution
        
    def plotData(self, xscale=1.5, yscale=1.0, xshift=2, yshift=2,
                 xzoom=0.5, yzoom=0.5, xstretch=1, ystretch=1):
        x_dim = self.x_dim
        y_dim = self.y_dim
        resolution=self.resolution
        A = np.zeros([y_dim, x_dim])   
        
        for x in range(x_dim):
            for y in range(y_dim):
                zx = self.initCoord(x, x_dim, xscale,
                                    xshift, xzoom, xstretch)
                zy = self.initCoord(y, y_dim, yscale,
                                    yshift, yzoom, ystretch)

                self.generateData(A, x, y, resolution, zx, zy)
                
        plt.imshow(A)
        plt.savefig('refactoring_1_refactored_code.png')
        plt.show()
    
    def initCoord(self, pixel, dim, scale, shift, zoom, stretch):
        return scale * (pixel - dim/shift) / (zoom * stretch * dim)

        
if __name__ == "__main__":
    # command line interface
    parser = ArgumentParser(description="Produce a Julia pattern")
    parser.add_argument('x_axis_limit', type=int,
                        help='x_dimension of Julia graph')
    parser.add_argument('y_axis_limit', type=int,
                        help='y_dimension of Julia graph')
    parser.add_argument('resolution', nargs='?', default=255, type=int,
                        help='depth of the image')
    arguments = parser.parse_args()

    
    initial = julia(arguments.x_axis_limit, arguments.y_axis_limit,
                  arguments.resolution)
    initial.plotData()
    



