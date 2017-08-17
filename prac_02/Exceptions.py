"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the Numerator/Denominator are not numbers.
2. When will a ZeroDivisionError occur?
    When the denominator is a 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Add a line in the text print stating not to use 0. 
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (Any number but 0): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")