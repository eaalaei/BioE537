# Component Specification

## 1. Introduction

This document outlines the major components and their specifications for a software application designed to simulate fluid flow inside tissue, determine the optimum suction velocity, and generate relevant plots using PyQt, DarcyTools, and Pyomo packages.

## 2. GUI Component

### 2.1 Functionality

The GUI component is responsible for collecting user inputs required for the simulation. It includes fields for:
- Size of the tissue (X and Y dimensions).
- Minimum and maximum allowable shear stress (maximum is mandatory, and minimum defaults to 0 if not provided).
- Permeability of the tissue.
- Density and viscosity of the fluid.

### 2.2 Input

- Size of the tissue (X and Y dimensions).
- Minimum and maximum allowable shear stress.
- Permeability of the tissue.
- Density and viscosity of the fluid.

### 2.3 Output

None (GUI is an input component).

## 3. Simulation Component (DarcyTools)

### 3.1 Functionality

The simulation component utilizes the DarcyTools package to simulate fluid flow within the tissue based on the provided inputs. It calculates shear stress, pathlines, pressure distribution, and velocity distribution.

### 3.2 Input

- Size of the tissue (X and Y dimensions).
- Minimum and maximum allowable shear stress.
- Permeability of the tissue.
- Density and viscosity of the fluid.

### 3.3 Output

- Shear stress data.
- Pathline plots.
- Pressure distribution plots.
- Velocity distribution plots.

## 4. Optimization Component (Pyomo)

### 4.1 Functionality

The optimization component, using the Pyomo package, determines the optimum suction velocity within the tissue.

### 4.2 Input

- Size of the tissue (X and Y dimensions).
- Minimum and maximum allowable shear stress.
- Permeability of the tissue.
- Density and viscosity of the fluid.

### 4.3 Output

- Optimum suction velocity in m/s.

## 5. Overall Output

- Suction velocity in m/s.
- Plots:
  - Shear stress plots.
  - Pathline contours.
  - Pressure distribution contours.
  - Velocity distribution contours.

## 6. Conclusion

This Component Specification provides a detailed overview of the major components, their functionalities, and the interactions necessary for simulating fluid flow within tissue. The outlined specifications serve as a guide for implementing and understanding the software architecture.
