# BioE537

## Porous Media Fluid Flow
This software is going to simulate fluid flow inside tissue, using the pressure distribution we would be able to calculate the shear stress. 
We use finite difference method to solve the related PDE and GUI to interact with user and showing the pressure distribution.
### Darcy's Law for Pressure Distribution

The Darcy pressure distribution in porous media is described by Darcy's law:

\[ Q = -k A \frac{\Delta P}{\mu L} \]

Where:
- \( Q \) is the volumetric flow rate,
- \( k \) is the permeability of the porous medium,
- \( A \) is the cross-sectional area through which the fluid flows,
- \( \Delta P \) is the pressure drop across the porous medium,
- \( \mu \) is the dynamic viscosity of the fluid,
- \( L \) is the length of the porous medium.

### Poisson Equation for Pressure

The Poisson equation for pressure in porous media is expressed as:

\[ \nabla \cdot \left( -k \nabla P \right) = \frac{\rho}{\mu} \frac{dQ}{dt} \]

Where:
- \( P \) is the pressure,
- \( k \) is the permeability of the porous medium,
- \( \nabla \) is the del operator representing the gradient,
- \( \rho \) is the fluid density,
- \( \mu \) is the dynamic viscosity of the fluid,
- \( \frac{dQ}{dt} \) is the rate of change of volumetric flow with respect to time.

### Shear Stress Calculation

The shear stress (\( \tau \)) in porous media can be calculated using Darcy's law:

\[ \tau = -k \frac{\Delta P}{L} \]

Where:
- \( \tau \) is the shear stress,
- \( k \) is the permeability of the porous medium,
- \( \Delta P \) is the pressure drop across the porous medium,
- \( L \) is the length of the porous medium.

### Porous Media Fluid Flow

Fluid flow through porous media is a common phenomenon in various natural and engineered systems. Porous media, such as soil, rock, or synthetic materials, contain interconnected void spaces through which fluids can move. The interaction between the fluid and the porous structure is crucial in understanding transport phenomena.

The permeability (\( k \)) of the porous medium determines how easily fluid can flow through it. Darcy's law relates the flow rate to the pressure drop, providing a fundamental understanding of porous media fluid dynamics.

The Poisson equation for pressure further describes the spatial variation of pressure within the porous medium, considering factors like fluid density (\( \rho \)), dynamic viscosity (\( \mu \)), and the rate of change of volumetric flow (\( \frac{dQ}{dt} \)).

Understanding and modeling porous media fluid flow are essential in various fields, including hydrogeology, petroleum engineering, and environmental science.
