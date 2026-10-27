class FigureColor:

    def __init__(self, color):
        self._color = color

    # свойство: чтение и запись цвета
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
