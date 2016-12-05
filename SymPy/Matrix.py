__auth__ = 'NguyenTTin'

from sympy import *
from sympy import Matrix
init_printing(use_unicode=True)

A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A*A)