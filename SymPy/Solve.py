__auth__ = 'NguyenTTin'

from sympy import *
x, y, z, t = symbols('x y z t')

print(solve(2*x - 1, x))
print(solve(x**2 - 1, x))
print(solve(x**3 + 1, x))
print(solve(x**2 - y**2))
print(solve((x + 5*y - 2, -3*x + 6*y - 15), x, y))
print(solve(x**3 + 3*x**2 + 2*x + 1))
print(solve(sin(x)+ cos(x) - 0.5))
print(solve(sin(x)+ cos(x) - 1))
print(solve_linear(x + y**2))
print(solve_linear(1/x - y**2))