# Geometric Brownian Motion Discretization Methods

This repository contains implementations of the Euler and Milstein discretization methods used to simulate paths of geometric Brownian motion (GBM). GBM is a stochastic process commonly used to model the price of financial instruments such as stocks.

## Overview

GBM is described by the stochastic differential equation (SDE):

\[ dX_t = \mu X_t dt + \sigma X_t dW_t \]

where:
- \( X_t \) is the stock price at time \( t \),
- \( \mu \) is the drift coefficient,
- \( \sigma \) is the volatility coefficient,
- \( W_t \) is a Wiener process or Brownian motion.

### Euler Discretization

The Euler method is a numerical technique for solving SDEs where the continuous time is divided into discrete intervals. The GBM is approximated as follows for small \( \Delta t \):

\[ X_{t+\Delta t} \approx X_t + \mu X_t \Delta t + \sigma X_t \sqrt{\Delta t} Z_t \]

with \( Z_t \) being a standard normal random variable.

### Milstein Discretization

The Milstein method introduces an additional term to account for the change in the diffusion part of the SDE, giving a more accurate approximation:

\[ X_{t+\Delta t} \approx X_t + \mu X_t \Delta t + \sigma X_t \sqrt{\Delta t} Z_t + \frac{1}{2} \sigma^2 X_t (\Delta t) (Z_t^2 - 1) \]


## Installation

No additional libraries are required for the execution of these scripts beyond the Python Standard Library.


## Usage

Example command-line instructions for running the script:

```bash
python discretization_methods.py
