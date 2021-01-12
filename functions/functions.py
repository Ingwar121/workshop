import math
from abc import ABC, abstractmethod


class FunctionImplementation(ABC):
    def __init__(self, *args, **kwargs):
        self._solutions = list()
        self._errors = list()
        self.validate_values()
        if self._errors:
            raise ValueError(self._errors)

    @abstractmethod
    def validate_values(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    @property
    def answer(self):
        if not self._solutions:
            raise SyntaxError('You should run .solve() method first!')
        return self._solutions


class QuadraticFunction(FunctionImplementation):
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
        super().__init__(a, b, c)

    def validate_values(self):
        if self.a == 0:
            self._errors.append('Parameter \'a\' should not be equal zero')

    def solve(self):
        d = self.b**2 - 4 * self.a * self.c
        if d < 0:
            raise ValueError('x can not be found')
        elif d > 0:
            x = (-self.b + d ** 0.5) / (2 * self.a)
            self._solutions.append(x)
            x = (-self.b - d ** 0.5) / (2 * self.a)
            self._solutions.append(x)
        else:
            x = -self.b / (2 * self.a)
            self._solutions.append(x)


class CircleAreaFunction(FunctionImplementation):
    def __init__(self, r: int):
        self.r = r
        super().__init__(r)

    def validate_values(self):
        if self.r <= 0:
            self._errors.append('Radius should be positive integer')

    def solve(self):
        self._solutions.append(self.r ** 2 * math.pi)


class SquareAreaFunction(FunctionImplementation):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__(a, b)

    def validate_values(self):
        if self.a <= 0:
            self._errors.append('a should be greater than zero')
        if self.b <= 0:
            self._errors.append('b should be greater than zero')

    def solve(self):
        self._solutions.append(self.a * self.b)
