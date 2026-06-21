class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            print(f"Width must be positive")

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            print(f"Height must be positive")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")


rect = Rectangle(5, 10)
rect.width = 4
rect.height = 8
del rect.width
del rect.height
print(rect.width)
print(rect.height)
