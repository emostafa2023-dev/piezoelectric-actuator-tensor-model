# Tensor Modeling of a Piezoelectric Actuator for Precision Positioning Systems

## Overview

This project implements a tensor-based mathematical model of a PZT-5H piezoelectric actuator.

The implementation includes:

- inverse piezoelectric effect modeling;
- Voigt notation for tensor representation;
- computation of normal and shear strains;
- stress analysis using the generalized Hooke's law;
- blocking force estimation;
- 3D visualization of actuator deformation.

## Technologies

- Python
- NumPy
- Matplotlib

## Physical Model

The model uses:

- Piezoelectric tensor **d**
- Elastic stiffness tensor **C**
- Voigt notation
- Inverse piezoelectric constitutive equations

## Repository Structure

- `tensor_calculation.py` — tensor strain computation
- `actuator_visualization.py` — 3D deformation visualization
- `actuator_tensor_model.py` — complete actuator model including stress and blocking force calculations
- `report.pdf` — project report

## Results

The simulation computes:

- longitudinal deformation;
- transverse deformation;
- shear deformation;
- mechanical stress;
- blocking force.

The generated visualization demonstrates the deformation of the actuator under an applied electric field with an enlarged scale factor for analysis.

## Author

Mostafa E. A. A. M.
