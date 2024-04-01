import math

# Function to evaluate (change this according to your function)
def evaluate_function(x, function_choice):
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
            return math.log(x)  # Handling log(0) case
        else:
            return float('inf')  # Handling log(0) case
    elif function_choice == 'f':
        return x ** power
    elif function_choice == 'g':
        return math.cos(x) ** -1  # Derived form

# Trapezoidal rule for numerical integration
def numerical_integration(a, b, subdivisions, function_choice):
    width = (b - a) / subdivisions  # Calculate the width of each subdivision
    result = 0  # Initialize the result
    for i in range(subdivisions + 1):
        xi = a + i * width  # Calculate the current value of x
        if i == 0 or i == subdivisions:
            result += evaluate_function(xi, function_choice) * math.e  # Add the function value multiplied by e
        else:
            result += 2 * evaluate_function(xi, function_choice) * math.e  # For inner points, multiply by 2 and add
    result *= width / 2  # Multiply the sum by the width of each subdivision and divide by 2 (Trapezoidal rule)
    return result

# Analytical integral for different functions
def analytical_integration(a, b, function_choice):
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
        power = 2  # Change the value of power as desired
        return ((b ** (power + 1) - a ** (power + 1)) / (power + 1))
    elif function_choice == 'g':
        return math.log(math.tan((b + math.pi / 2) / 2)) - math.log(math.tan((a + math.pi / 2) / 2))

# Input limits of integration
lower_limit = float(input("Enter the lower limit of integration (a): ")) 
upper_limit = float(input("Enter the upper limit of integration (b): "))

# Number of subdivisions
subdivisions = int(input("Enter the number of subdivisions (n): "))

# Choose the function
function_choices = {
    'a': 'cos(x)',
    'b': 'sin(x)',
    'c': 'tan(x)',
    'd': 'exp(x)',
    'e': 'log(x)',
    'f': 'x^n',
    'g': '1 / cos(x)'
}

print("Choose the function to integrate ('a' to 'g')")
for choice, function_description in function_choices.items():
    print(f"{choice}: {function_description}")

function_choice = input("Enter your choice: ")

# Perform numerical integration
integral = numerical_integration(lower_limit, upper_limit, subdivisions, function_choice)
print("Integral (Cartesian form):", integral)

# Convert integral to polar form
integral_polar = abs(integral) * math.e ** (1j * math.atan2(integral.imag, integral.real))
print("Integral (Polar form):", integral_polar)

# Analytical result
analytical_result = analytical_integration(lower_limit, upper_limit, function_choice)
print("Analytical result:", analytical_result)

# Difference between numerical and analytical results
error = abs(integral - analytical_result)
print("Absolute Error:", error)