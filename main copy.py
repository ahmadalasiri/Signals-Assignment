import math

def select_function(x, function_choice):
    """
    Selects the function to be integrated based on the function choice.
    
    Args:
        x (float): The value at which the function is evaluated.
        function_choice (str): The choice of function to integrate (a-g).
    
    Returns:
        float: The value of the selected function at x.
    """
    if function_choice == 'a':
        return math.cos(x)
    elif function_choice == 'b':
        return math.sin(x)
    elif function_choice == 'c':
        return math.tan(x)
    elif function_choice == 'd':
        return math.exp(x)
    elif function_choice == 'e':
        return math.log(x) if x > 0 else float('inf')  # Handles log(0) case
    elif function_choice == 'f':
        return x ** n
    elif function_choice == 'g':
        return 1 / math.cos(x)

def trapezoidal_integration(a, b, n, function_choice):
    """
    Performs numerical integration using the Trapezoidal rule.
    
    Args:
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        n (int): Number of subdivisions.
        function_choice (str): The choice of function to integrate (a-g).
    
    Returns:
        float: The result of numerical integration.
    """
    h = (b - a) / n  # Calculate the width of each subdivision
    result = 0  # Initialize the result
    for i in range(n + 1):
        xi = a + i * h  # Calculate the current value of x
        weight = 2 if i == 0 or i == n else 1  # Weight for trapezoidal rule
        result += weight * select_function(xi, function_choice)  # Add the weighted function value
    result *= h / 2  # Multiply the sum by the width of each subdivision and divide by 2 (Trapezoidal rule)
    return result

def analytical_integration(a, b, function_choice):
    """
    Computes the analytical integral for different functions.
    
    Args:
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        function_choice (str): The choice of function to integrate (a-g).
    
    Returns:
        float: The analytical result of integration.
    """
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
        return (b ** (n + 1) - a ** (n + 1)) / (n + 1)
    elif function_choice == 'g':
        return math.log(math.tan((b + math.pi / 2) / 2)) - math.log(math.tan((a + math.pi / 2) / 2))

def main():
    """
    Main function to perform integration.
    """
    # Input limits of integration
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    n = int(input("Enter the number of subdivisions (n): "))

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
    integral = trapezoidal_integration(a, b, n, function_choice)
    print("Numerical integration result (Cartesian form):", integral)

    # Convert integral to polar form
    integral_polar = abs(integral) * math.e ** (1j * math.atan2(integral.imag, integral.real))
    print("Integral result (Polar form):", integral_polar)

    # Compute analytical result
    analytical_result = analytical_integration(a, b, function_choice)
    print("Analytical result:", analytical_result)

    # Compute absolute error
    error = abs(integral - analytical_result)
    print("Absolute Error:", error)

if __name__ == "__main__":
    main()
