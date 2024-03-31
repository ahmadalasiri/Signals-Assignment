# Integration Script README

## Introduction
This script performs numerical integration using the Trapezoidal rule and compares the results with analytical integrals for various mathematical functions.

## Overview
The `main.py` Python script defines functions for numerical integration, analytical integration, and user interaction.

## Functionality
- `f(x, function_choice)`: Defines mathematical functions based on user choice.
- `integrate(a, b, n, function_choice)`: Implements Trapezoidal rule for numerical integration.
- `analytical_integral(a, b, function_choice)`: Computes analytical integral for different functions.

## Usage
1. Input lower and upper limits of integration (a and b).
2. Specify the number of subdivisions (n).
3. Choose the function to integrate (a-g).

## Results
- Displayed integral in Cartesian form.
- Converted integral to Polar form.
- Analytical result.
- Absolute error between numerical and analytical results.

## Installation
No additional dependencies required. Simply run `python main.py`.

## Examples
- Integrating `sin(x)` from 0 to pi: `a=0`, `b=3.14159`, `n=100`, `function_choice=b`.
 
 
