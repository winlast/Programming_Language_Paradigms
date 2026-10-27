import sys
import math


# коэффициент из командной строки, иначе ввод с клавиатуры до корректного значения
def get_coef(index, prompt):
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


def get_discriminant(a, b, c):
    return b*b - 4*a*c


def get_roots(a, b, c):
    D = get_discriminant(a, b, c)
    # корни относительно t = x²
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
    # обратная замена: x = ±√t
    result = []
    for t in square_roots:
        if t == 0.0:
            result.append(0.0)
        elif t > 0.0:
            result.append(-math.sqrt(t))
            result.append(math.sqrt(t))
    return sorted(result)


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    if a == 0.0 and b == 0.0 and c == 0.0:
        print('Корень - любое число')
        return
    if a == 0.0:
        print('A = 0, уравнение не биквадратное')
    else:
        print('Дискриминант: {}'.format(get_discriminant(a, b, c)))
    roots = get_roots(a, b, c)
    if len(roots) == 0:
        print('Нет действительных корней')
    else:
        print('Корни: {}'.format(', '.join(str(root) for root in roots)))


if __name__ == "__main__":
    main()
