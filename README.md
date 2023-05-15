# Solving-Convection-Diffusion-Problems

title: "Solving convection-diffusion problems"
author: Yang, Jiayu ; Silvester, David.
date: "2023-05-06"
keywords: numerical solutions of PDEs, convection-diffusion problems, FDM, FEM, FVM, PINN

## Introduction

The project aims to find accurate and efficient numerical solutions to the one- and two-dimensional steady convection-diffusion equations.
This code base supports all display images used in the project, except for the reference diagram.
The methods we will use are respectively listed below.

## 1. FDM Finite Difference Method

FDM is often suitable for problems with regular grid structures and simple geometries, such as problems defined on rectangular or Cartesian grids. It is particularly effective for problems with smooth solutions and isotropic properties. FDM is relatively straightforward to implement and computationally efficient for structured grids. FDM is a good choice when accuracy requirements are moderate and the solution behavior is well-understood.

### 1.1 FDM with Central Difference Scheme

### 1.2 FDM with Artificial Difference Scheme

### 1.3 FDM with Upwind Difference Scheme

## 2. FEM Finite Element Method

FEM is well-suited for problems with complex geometries, irregular domains, and problems that involve heterogeneous or anisotropic materials. It offers flexibility in handling arbitrary geometries by using unstruc- tured or adaptive meshes. FEM is particularly effective for problems with localized phenomena, such as stress concentrations or boundary layers. It provides accurate solutions and allows for the inclusion of various boundary conditions and material properties. FEM is widely used in structural mechanics, heat transfer, and fluid dynamics.

### 2.1 FEM with Galerkin Approximation Scheme

### 2.2 FEM with Petrov-Galerkin Approximation Scheme


## 3. FVM Finite Volume Method

FVM is often chosen for problems with conservation laws, such as fluid flow, heat transfer, or mass transport problems. It is suitable for problems involving control volumes or cells, where the solution is discretized at the center of each cell. FVM naturally ensures the conservation of quantities across the cell interfaces and is robust for capturing shocks, discontinuities, or strong gradients. FVM is commonly used in computational fluid dynamics (CFD) and has applications in various engineering disciplines. It is particularly suitable for problems with complex flow behaviors, such as turbulent flows or multiphase flows.

### 3.1 FVM with Central Difference Scheme

### 3.2 FVM with Upwind Difference Scheme

### 3.3 FVM with Hybrid Difference Scheme


It’s important to note that the choice between FDM, FEM, and FVM is not always mutually exclusive, and there can be overlaps depending on the specific problem and the available computational resources. Researchers often select the method that best matches the problem requirements in terms of accuracy, efficiency, and the ability to handle the desired geometries and physics.
