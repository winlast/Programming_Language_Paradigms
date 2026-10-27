import math
import unittest

from lab_python_oop.figure import Figure
from lab_python_oop.color import FigureColor
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestFigures(unittest.TestCase):

    def test_figure_is_abstract(self):
        # объект абстрактного класса создать нельзя
        with self.assertRaises(TypeError):
            Figure()

    def test_color_property(self):
        figure_color = FigureColor('синего')
        figure_color.color = 'желтого'
        self.assertEqual(figure_color.color, 'желтого')

    def test_rectangle(self):
        rectangle = Rectangle(25, 25, 'синего')
        self.assertEqual(rectangle.area(), 625)
        self.assertEqual(Rectangle.get_figure_type(), 'Прямоугольник')
        self.assertEqual(repr(rectangle),
                         'Прямоугольник синего цвета шириной 25 и высотой 25 площадью 625.')

    def test_circle(self):
        circle = Circle(25, 'зеленого')
        self.assertAlmostEqual(circle.area(), math.pi * 625)
        self.assertEqual(Circle.get_figure_type(), 'Круг')
        self.assertEqual(repr(circle),
                         'Круг зеленого цвета радиусом 25 площадью 1963.50.')

    def test_square(self):
        square = Square(25, 'красного')
        self.assertIsInstance(square, Rectangle)
        self.assertEqual(square.area(), 625)
        self.assertEqual(Square.get_figure_type(), 'Квадрат')
        self.assertEqual(repr(square),
                         'Квадрат красного цвета со стороной 25 площадью 625.')


if __name__ == '__main__':
    unittest.main()
