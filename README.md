# Solving-Convection-Diffusion-Problems

title: "Solving convection-diffusion problems" 
author: Yang, Jiayu ; Silvester, David. 
date: "2023-05-06" 
keywords: numerical solutions of PDEs, convection-diffusion problems, FDM, FEM, FVM, PINN

## Introduction

The project aims to find accurate and efficient numerical solutions to the one- and two-dimensional steady convection-diffusion equations. This code base supports all display images used in the project, except for the reference diagram. The methods we will use are respectively listed below.

## 1. FDM Finite Difference Method

FDM is often suitable for problems with regular grid structures and simple geometries, such as problems defined on rectangular or Cartesian grids. It is particularly effective for problems with smooth solutions and isotropic properties. FDM is relatively straightforward to implement and computationally efficient for structured grids. FDM is a good choice when accuracy requirements are moderate and the solution behavior is well-understood.

### 1.1 FDM with Central Difference Scheme

![FDM Central Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FDM%20Central%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

Image Outputs/2D Comparison of FDM with different schemes at Pe = 1.0.png

### 1.2 FDM with Artificial Difference Scheme

![FDM Artificial Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FDM%20Artificial%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### 1.3 FDM with Upwind Difference Scheme

![FDM Upwind Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FDM%20Upwind%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### Comparison of FDM with different schemes

![Different FDM Schemes under different Peclet numbers at N = 10](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/Differnt%20FDM%20Schemes%20under%20different%20Pe%20at%20N%20=%2010.png){width="500"}

## 2. FEM Finite Element Method

FEM is well-suited for problems with complex geometries, irregular domains, and problems that involve heterogeneous or anisotropic materials. It offers flexibility in handling arbitrary geometries by using unstruc- tured or adaptive meshes. FEM is particularly effective for problems with localized phenomena, such as stress concentrations or boundary layers. It provides accurate solutions and allows for the inclusion of various boundary conditions and material properties. FEM is widely used in structural mechanics, heat transfer, and fluid dynamics.

### 2.1 FEM with Galerkin Approximation Scheme

![FEM Galerkin Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FEM%20Galerkin%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### 2.2 FEM with Petrov-Galerkin Approximation Scheme

![FEM Petrov Galerkin Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FEM%20Petrov%20Galerkin%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### Comparison of FEM with different schemes

![Differnt FEM Schemes under different Pe at N = 10](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/Differnt%20FEM%20Schemes%20under%20different%20Pe%20at%20N%20=%2010.png){width="936"}

## 3. FVM Finite Volume Method

FVM is often chosen for problems with conservation laws, such as fluid flow, heat transfer, or mass transport problems. It is suitable for problems involving control volumes or cells, where the solution is discretized at the center of each cell. FVM naturally ensures the conservation of quantities across the cell interfaces and is robust for capturing shocks, discontinuities, or strong gradients. FVM is commonly used in computational fluid dynamics (CFD) and has applications in various engineering disciplines. It is particularly suitable for problems with complex flow behaviors, such as turbulent flows or multiphase flows.

### 3.1 FVM with Central Difference Scheme

![FVM Central Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FVM%20Central%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### 3.2 FVM with Upwind Difference Scheme

![FVM Upwind Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FVM%20Upwind%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

### 3.3 FVM with Hybrid Difference Scheme

![FVM Hybrid Scheme at N = 10 under different Peclet numbers](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/FVM%20Hybrid%20Scheme_N%20=%2010%20under%20different%20Pe.png){width="375"}

## Comparison of FVM with different schemes

![Differnt FVM Schemes under different Pe at N = 10](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/Differnt%20FVM%20Schemes%20under%20different%20Pe%20at%20N%20=%2010.png){width="500"}

## 4. 2D FDM with Central, Artificial, Upwind Schemes Outputs

|                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![2D Comparison of FDM with different schemes at Pe = 1.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FDM%20with%20different%20schemes%20at%20Pe%20=%201.0.png)   |
| ![2D Comparison of FDM with different schemes at Pe = 5.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FDM%20with%20different%20schemes%20at%20Pe%20=%205.0.png)   |
| ![2D Comparison of FDM with different schemes at Pe = 10.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FDM%20with%20different%20schemes%20at%20Pe%20=%2010.0.png) |

## 5. 2D FEM with Galerkin and Petrov-Galerkin Schemes Outputs

|                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![2D Comparison of FEM with different schemes at Pe = 0.5](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FEM%20with%20different%20schemes%20at%20Pe%20=%200.5.png)   |
| ![2D Comparison of FEM with different schemes at Pe = 1.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FEM%20with%20different%20schemes%20at%20Pe%20=%201.0.png)   |
| ![2D Comparison of FEM with different schemes at Pe = 5.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FEM%20with%20different%20schemes%20at%20Pe%20=%205.0.png)   |
| ![2D Comparison of FEM with different schemes at Pe = 10.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FEM%20with%20different%20schemes%20at%20Pe%20=%2010.0.png) |

## 6. 2D FVM with Central, Upwind, Hybrid Schemes Outputs

|                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![2D Comparison of FVM with different schemes at Pe = 0.5](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FVM%20with%20different%20schemes%20at%20Pe%20=%200.5.png)   |
| ![2D Comparison of FVM with different schemes at Pe = 1.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FVM%20with%20different%20schemes%20at%20Pe%20=%201.0.png)   |
| ![2D Comparison of FVM with different schemes at Pe = 5.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FVM%20with%20different%20schemes%20at%20Pe%20=%205.0.png)   |
| ![2D Comparison of FVM with different schemes at Pe = 10.0](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/2D%20Comparison%20of%20FVM%20with%20different%20schemes%20at%20Pe%20=%2010.0.png) |

## 7. Physical Informed Neural Networks (PINN)

|                                                                                                                                                              |                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![PINN Solution at Pe = 0.5, N = 10](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/PINN%20Solution%20at%20Pe%20=%200.5,%20N%20=%2010.png) | ![PINN Solution at Pe = 10.0, N = 10](Desktop/Solving%20Convection-Diffusion%20Problem/Image%20Outputs/PINN%20Solution%20at%20Pe%20=%2010,%20N%20=%2010.png) |

## Comments

The choice between FDM, FEM, and FVM is not always mutually exclusive, and there can be overlaps depending on the specific problem and the available computational resources. Researchers often select the method that best matches the problem requirements in terms of accuracy, efficiency, and the ability to handle the desired geometries and physics.
