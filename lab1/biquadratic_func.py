import sys
import math
from typing import NamedTuple


# алгебраический тип: корни уравнения относительно t = x²
class SquareRootResult:
    NoRoots = NamedTuple("NoRoots", [])
    OneRoot = NamedTuple("OneRoot", [("root", float)])
    TwoRoots = NamedTuple("TwoRoots", [("root1", float), ("root2", float)])
    AnyRoot = NamedTuple("AnyRoot", [])


def parse_coef(coef_str):
    try:
        return float(coef_str)
    except ValueError:
        return None


# повторный ввод через рекурсию вместо цикла
def read_coef(prompt):
    print(prompt)
    match parse_coef(input()):
        case float(coef):
            return coef
        case _:
            return read_coef(prompt)


def get_coef(index, prompt):
    match [parse_coef(arg) for arg in sys.argv[index:index + 1]]:
        case [float(coef)]:
            return coef
        case _:
            return read_coef(prompt)


def get_discriminant(a, b, c):
    return b*b - 4*a*c


def get_square_roots(a, b, c):
    # A = 0: уравнение B·t + C = 0
    match (a, b, c):
        case (0, 0, 0):
            return SquareRootResult.AnyRoot()
        case (0, 0, _):
            return SquareRootResult.NoRoots()
        case (0, _, _):
            return SquareRootResult.OneRoot(-c / b)
    match get_discriminant(a, b, c):
        case 0:
            return SquareRootResult.OneRoot(-b / (2.0*a))
        case D if D > 0:
            sqD = math.sqrt(D)
            return SquareRootResult.TwoRoots((-b + sqD) / (2.0*a), (-b - sqD) / (2.0*a))
        case _:
            return SquareRootResult.NoRoots()


# обратная замена: решение x² = t
def roots_from_square(t):
    match t:
        case 0:
            return (0.0,)
        case t if t > 0:
            return (-math.sqrt(t), math.sqrt(t))
        case _:
            return ()


def get_roots(a, b, c):
    match get_square_roots(a, b, c):
        case SquareRootResult.AnyRoot():
            return None
        case SquareRootResult.NoRoots():
            return ()
        case SquareRootResult.OneRoot(t):
            return roots_from_square(t)
        case SquareRootResult.TwoRoots(t1, t2):
            return tuple(sorted(roots_from_square(t1) + roots_from_square(t2)))


def discriminant_text(a, b, c):
    match (a, b, c):
        case (0, 0, 0):
            return None
        case (0, _, _):
            return 'A = 0, уравнение не биквадратное'
        case _:
            return 'Дискриминант: {}'.format(get_discriminant(a, b, c))


def roots_text(roots):
    match roots:
        case None:
            return 'Корень - любое число'
        case ():
            return 'Нет действительных корней'
        case _:
            return 'Корни: {}'.format(', '.join(str(root) for root in roots))


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    match discriminant_text(a, b, c):
        case str(text):
            print(text)
    print(roots_text(get_roots(a, b, c)))


if __name__ == "__main__":
    main()
