import numpy

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

N = 25


def main():
    rectangle = Rectangle(N, N, 'синего')
    circle = Circle(N, 'зеленого')
    square = Square(N, 'красного')
    print(rectangle)
    print(circle)
    print(square)
    # вызов метода внешнего пакета numpy
    total_area = numpy.sum([rectangle.area(), circle.area(), square.area()])
    print('Суммарная площадь фигур (numpy.sum): {:.2f}'.format(total_area))


if __name__ == '__main__':
    main()
