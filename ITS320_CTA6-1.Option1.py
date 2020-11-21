#------------------------------------------------------------------------
# Program Name: Working with Python Classes
# Program Author: Jason Myers
# Program Objective: given two complex numbers, print the result of their
#                     addition, subtraction, multiplication, division, and
#                     modulus operations.
#                     The real and imaginary precision part should be
#                     correct up to two decimal places.
#-----------------------------------------------------------------------
# Pseudocode:
#           Import Math
#           Defined class to do all the math functions
#           Print results
#------------------------------------------------------------------------
# Program Inputs: 2 sets of numbers
# Program Outputs: Math of each set of numbers 
#------------------------------------------------------------------------

import math  # Import math module

class Complex(object): # Create class to do all the math
  def __init__(self, real, imaginary):
    self.real = real
    self.imaginary = imaginary

# Addition
  def __add__(self, no):
    real = (self.real + no.real)
    imaginary = (self.imaginary + no.imaginary)
    return Complex(real, imaginary)
  
# Subtraction
  def __sub__(self, no): 
    real = (self.real - no.real)
    imaginary = (self.imaginary - no.imaginary)   
    return Complex(real, imaginary)

# Multiplication
  def __mul__(self, no):
    real = ((self.real * no.real) - (self.imaginary * no.imaginary))
    imaginary = ((self.real * no.imaginary) + (self.imaginary * no.real))
    return Complex(real, imaginary)

# Division
  def __truediv__(self, no):
    x = ((no.real ** 2) + (no.imaginary ** 2))
    real = (((self.real * no.real) + (self.imaginary * no.imaginary)) / x)
    imaginary = (((self.imaginary * no.real) - (self.real * no.imaginary)) / x) 
    return Complex(real, imaginary)

# Modulus
  def mod(self):
    real = math.sqrt((self.real ** 2) + (self.imaginary ** 2))
    return Complex(real, 0)

# String it all together
  def __str__(self):
    if self.imaginary == 0:
      result = '%.2f+0.00i' % (self.real)
    elif self.real == 0:
      if self.imaginary >= 0:
        result = '0.00+%.2fi' % (self.imaginary)
      else:
        result = '0.00-%.2fi' % (abs(self.imaginary))
    elif self.imaginary > 0:
      result = '%.2f+%.2fi' % (self.real, self.imaginary)
    else:
      result = '%.2f-%.2fi' % (self.real, abs(self.imaginary))
    return result

if __name__ == '__main__' :
  # Set variable for loop
  i = 0

  # Create loop to allow for running program again
  while i < 1:
    # Error checking loop
    while True:
      try:
        C = map(float, input('\nEnter the real and imaginary parts of the first complex number (separated by a space): ').split())
        D = map(float, input('\nEnter the real and imaginary parts of the second complex number (separated by a space): ').split())
        x = Complex(*C)
        y = Complex(*D)
        print('\n', '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()])))
        break
      except:
        print('\nEnter the real and then the imaginary parts of the complex number. \n' ,
              u"\u2022", 'Make sure there is a space in between each set of numbers. \n',
              u"\u2022", 'Omit the "i." \n',
              u"\u2022", 'Do not include a "0" for the denominator. \n',
              u"\u2022", 'You can only enter numbers \n')
    # Ask if user want to run again
    question=input('\nDo you want to check any other numbers? ')
    if question=='n' or question=='N' or question=='No' or question=='no':
      i = 1
