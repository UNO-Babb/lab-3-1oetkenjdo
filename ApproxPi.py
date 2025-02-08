#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time

# Function to approximate Pi using Leibniz formula
def approximate_pi(precision):
    pi_approx = 0
    # Leibniz formula: pi = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
    for i in range(precision):
        term = 4 * ((-1) ** i) / (2 * i + 1)
        pi_approx += term
    return pi_approx

def main():
    realPi = math.pi

    # Ask the user for decimal precision (up to 15)
    decimal_places = int(input("Enter the number of decimal places of precision (up to 15): "))
    
    if decimal_places < 1 or decimal_places > 15:
        print("Please enter a valid number between 1 and 15")
        return

    # Start timing the approximation
    start = time.time()

    # Calculate pi using the approximation technique
    precision = 1000000  # The number of terms to sum in the Leibniz series (increase for better precision)
    approximated_pi = approximate_pi(precision)
    
    # Round the approximated value to the desired decimal places
    approximated_pi_rounded = round(approximated_pi, decimal_places)
    
    # Stop timing the approximation
    end = time.time()

    elapsedTime = end - start

    # Output the results
    #print(f"Real Pi value: {realPi}") TO ME I DONT NEED IT FOR THE OUTPUT...
    print(f"Approximated Pi value (to {decimal_places} decimal places): {approximated_pi_rounded}")
    print(f"Time taken to compute the approximation: {elapsedTime:.5f} seconds")

if __name__ == '__main__':
    main()