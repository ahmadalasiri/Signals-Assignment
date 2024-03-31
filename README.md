# Integration Script README

## Introduction
This script performs numerical integration using the Trapezoidal rule and compares the results with analytical integrals for various mathematical functions.

## Overview
The `main.py` Python script defines functions for numerical integration, analytical integration, and user interaction.

## Functionality
- `f(x, function_choice)`: This function takes a value `x` and a function choice (`a-g`) and returns the corresponding mathematical function value. It supports several standard mathematical functions including cosine, sine, tangent, exponential, and logarithm. Additionally, it can handle a user-defined power function (`x^n`) and the inverse cosine function.
  
- `integrate(a, b, n, function_choice)`: Implements the Trapezoidal rule for numerical integration over the interval `[a, b]` with `n` subdivisions and the chosen function. It divides the interval into `n` equal subdivisions and computes the area under the curve using the Trapezoidal rule. It handles different function choices by calling the `f` function appropriately.
  
- `analytical_integral(a, b, function_choice)`: Computes the analytical integral for different functions over the interval `[a, b]`. It provides analytical solutions for various functions including trigonometric functions, exponential function, logarithmic function, and power function. The analytical solutions are derived based on standard integration rules and formulas.

These functions collectively provide a comprehensive tool for both numerical and analytical integration of various functions, enabling users to accurately compute definite integrals over specified intervals.


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
 
 
