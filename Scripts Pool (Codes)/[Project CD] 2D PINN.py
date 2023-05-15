# -------------------------------------------------- #
# Author: Jiayu Yang
# Date: 15 May 2023
# File Name: [Project CD] 2D FDM with Central, Artificial, Upwind Difference Scheme
# File Description:
#    This file aims at solving the 2D steady convection-diffusion problems using the
#    Finite Difference Method (FDM) with respectively:
#        - Central Difference Scheme
#        - Artificial Difference Scheme
#        - Upwind Difference Scheme
#    The comparison of stability is also included.
# Web Link to Github: https://github.com/LakeYang0818/Solving-Convection-Diffusion-Problems
# -------------------------------------------------- #

from pydens import Solver, D, V, ConvBlockModel
import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from mpl_toolkits import mplot3d
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
#%matplotlib widget
#%matplotlib inline

# Set up of Parameters
alpha = 200 # convective coefficient
nu = 1 # diffusive coefficient
s = 1 # source
N = 10 + 1 # number of partitions on both x-axis and y-axis
x = np.linspace(0, 1, N) # x-axis gridpoints
y = np.linspace(0, 1, N) # x-axis gridpoints

# Define the convection-diffusion equation
def pde(f, x, y):
    u = alpha * (D(f, x) + D(f, y)) \
        - nu * (D(D(f, x), x) + D(D(f, y), y)) \
        - torch.cos(np.pi*x) - s
    return u

# Neural Network Structure:
#     input  layer  = 1
#     hidden layers = 4
#     output layer  = 1
# activation function: tanh()
solver = Solver(equation=pde, ndims=2, boundary_condition = 1,
                layout = 'fa fa fa f', activation = 'Tanh', units = [10, 12, 15, 1])

# Fit the solver to the equation to optimize the parameters within the layers.
solver.fit(batch_size = 100, niters = 1500)

# Grid points basis of (x, y)
def cart_prod(*arrs):
    grids = np.meshgrid(*arrs, indexing='ij')
    return np.stack(grids, axis = -1).reshape(-1, len(arrs))
grid = cart_prod(x, y)

# Predict the values of u based on the network structure
approxs = solver.predict(grid[:, 0:1], grid[:, 1:2]).reshape((N, N))

# Plot the solutions to the convection-diffusion problems
def plot_approximation_3d(approximation):
    fig = plt.figure(figsize=(10,7))
    ax = fig.add_subplot(111, projection='3d')
    ax.invert_xaxis()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x,y)')
    ax.set_title('PINN Solution at Pe = 10, N = 10')
    surf=ax.plot_surface(grid[:, 0:1].reshape(N,N), grid[:, 1:2].reshape(N,N),approximation ,linewidth=0.1,cmap=cm.coolwarm)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    #plt.savefig('/Users/pc/Desktop/[P2] Convection-Diffusion Problem/Images Pool/PINN Solution at Pe = 10, N = 10.png')
    plt.show()

plot_approximation_3d(approxs)

