# A) Introduction to Python Programming. Installation & Configuration of Python. Along
# with its all-major editors, IDLE, Pycharm, Anaconda, Jupyter, Interpreter etc.
# B) Write a python program to calculate simple interest.

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period in years: "))

si = (p * r * t) / 100

print(" The simple interest is : ", si)