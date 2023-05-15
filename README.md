# Solving-Convection-Diffusion-Problems

title: "Solving convection-diffusion problems"
author: Yang, Jiayu ; Silvester, David.
date: "2023-05-06"

## Abstract

The accurate and efficient numerical solution of convection-diffusion equations plays a pivotal role in various scientific and engineering applications. In this paper, we present a comprehensive study on the performance of three popular numerical methods: Finite Difference Method (FDM), Finite Element Method (FEM), and Finite Volume Method (FVM) - to solving the one-dimensional steady convection-diffusion problem.

## Introduction

The convection-diffusion problem arises in numerous physical phenomena, such as fluid flow with simultaneous diffusion of a chemical concentration or the transport of pollutants in the atmosphere. It involves the interaction between convection which represents the transport of quantities due to volume motion, and diffusion which denotes the spreading or dissipation of quantities due to concentration gradients.

This combination often leads to challenging mathematical equations that are difficult to obtain analytical solutions, so we need numerical methods to solve them. The choice of an appropriate numerical method then becomes crucial to obtain reliable results that satisfy some basic properties. In this paper, we focus on five essential properties to evaluate the numerical methods:

1.  transportiveness
2.  consistency
3.  stability
4.  convergence
5.  conservativeness.

To satisfy these five properties, we will adopt and evaluate three widely employed numerical methods: the finite Difference Method (FDM), the Finite Element Method (FEM), and the Finite Volume Method (FVM).

We will first start with the traditional version of each method. For FDM, we will implement the Central Difference Scheme a widely used method known for its simplicity and ease of implementation. For FEM, we will employ the Galerkin Approximation Scheme, which allows for flexible meshing and efficient handling of complex geometries. Finally, we will use FVM with Central Difference Scheme that provides a conservative formulation and compatibility with control volume discretization.

After evaluating five properties of these traditional schemes in solving one-dimensional steady convection-diffusion problems, we propose improvements for each method to overcome the limitations of the traditional schemes. For FDM, we introduce the Upwind Difference Scheme and the Artificial Difference Scheme; for FEM, we adopt the Petrov-Galerkin (SUPG) Approximation Scheme; and finally, for FVM, we explore the Upwind Difference Scheme and Hybrid Difference Scheme.

By evaluating the performance of these three methods and their associated schemes, we aim to provide comparisons of numerical methods for solving convection-diffusion problems, helping to select the appropriate numerical method when solving problems under different physical situations.
