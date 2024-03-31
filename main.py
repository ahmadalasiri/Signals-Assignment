import math

# Function to integrate (change this according to your function)
def f(x, function_choice):
    if function_choice == 'a':
        return math.cos(x)
    elif function_choice == 'b':
        return math.sin(x)
    elif function_choice == 'c':
        return math.tan(x)
    elif function_choice == 'd':
        return math.exp(x)
    elif function_choice == 'e':
        if x > 0:
            return math.log(x)
        else:
            return float('inf')  # Handling log(0) case
    elif function_choice == 'f':
        return x**n
    elif function_choice == 'g':
        return math.cos(x)**-1  # Derived form

# Trapezoidal rule for numerical integration
def integrate(a, b, n, function_choice):
    h = (b - a) / n  # Calculate the width of each subdivision
    result = 0  # Initialize the result
    for i in range(n + 1):
        xi = a + i * h  # Calculate the current value of x
        if i == 0 or i == n:
            result += f(xi, function_choice) * math.e  # Add the function value multiplied by e
        else:
            result += 2 * f(xi, function_choice) * math.e  # For inner points, multiply by 2 and add
    result *= h / 2  # Multiply the sum by the width of each subdivision and divide by 2 (Trapezoidal rule)
    return result

# Analytical integral for different functions
def analytical_integral(a, b, function_choice):
    if function_choice == 'a':
        return math.sin(b) - math.sin(a)
    elif function_choice == 'b':
        return -math.cos(b) + math.cos(a)
    elif function_choice == 'c':
        return math.log(abs(math.cos(a) / math.cos(b)))
    elif function_choice == 'd':
        return math.exp(b) - math.exp(a)
    elif function_choice == 'e':
        return b * math.log(b) - a * math.log(a) - (b - a)
    elif function_choice == 'f':
        n = 2  # Change the value of n as desired
        return ((b**(n+1) - a**(n+1)) / (n + 1))
    elif function_choice == 'g':
        return math.log(math.tan((b + math.pi/2) / 2)) - math.log(math.tan((a + math.pi/2) / 2))

# Input limits of integration
a = float(input("Enter the lower limit of integration (a): ")) 
b = float(input("Enter the upper limit of integration (b): "))

# Number of subdivisions
n = int(input("Enter the number of subdivisions (n): "))

# Choose the function
function_choice = input("Choose the function to integrate (a-g): ")

# Perform numerical integration
integral = integrate(a, b, n, function_choice)
print("Integral (Cartesian form):", integral)

# Convert integral to polar form
integral_polar = abs(integral) * math.e**(1j * math.atan2(integral.imag, integral.real))
print("Integral (Polar form):", integral_polar)

# Analytical result
analytical_result = analytical_integral(a, b, function_choice)
print("Analytical result:", analytical_result)

# Difference between numerical and analytical results
error = abs(integral - analytical_result)
print("Absolute Error:", error)