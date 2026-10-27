import sys
import math


class BiquadraticEquation:

    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.discriminant = 0.0
        self.roots_list = []

    def get_coef(self, index, prompt):
        if index < len(sys.argv):
            try:
                return float(sys.argv[index])
            except ValueError:
                pass
        while True:
            print(prompt)
            try:
                return float(input())
            except ValueError:
                pass

    def get_coefs(self):
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        self.discriminant = b*b - 4*a*c
        D = self.discriminant
        square_roots = []
        if a == 0.0:
            if b != 0.0:
                square_roots.append(-c / b)
        elif D == 0.0:
            square_roots.append(-b / (2.0*a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            square_roots.append((-b + sqD) / (2.0*a))
            square_roots.append((-b - sqD) / (2.0*a))
        for t in square_roots:
            if t == 0.0:
                self.roots_list.append(0.0)
            elif t > 0.0:
                self.roots_list.append(-math.sqrt(t))
                self.roots_list.append(math.sqrt(t))
        self.roots_list.sort()

    def print_roots(self):
        if self.coef_A == 0.0 and self.coef_B == 0.0 and self.coef_C == 0.0:
            print('Корень - любое число')
            return
        if self.coef_A == 0.0:
            print('A = 0, уравнение не биквадратное')
        else:
            print('Дискриминант: {}'.format(self.discriminant))
        if len(self.roots_list) == 0:
            print('Нет действительных корней')
        else:
            print('Корни: {}'.format(', '.join(str(root) for root in self.roots_list)))


def main():
    eq = BiquadraticEquation()
    eq.get_coefs()
    eq.calculate_roots()
    eq.print_roots()


if __name__ == "__main__":
    main()
