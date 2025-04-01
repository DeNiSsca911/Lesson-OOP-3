#       Продемонстрировать принцип полиморфизма через реализацию разных классов,
#     представляющих геометрические формы, и метод для расчёта площади каждой формы.
# 1. Создать базовый класс Shape с методом area(), который просто возвращает 0.
# 2. Создать несколько производных классов для разных форм (например, Circle, Rectangle,
#     Square), каждый из которых переопределяет метод area().
# 3. В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# 4. Написать функцию, которая принимает объект класса Shape и выводит его площадь.
#from curses.textpad import rectangle


class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class  Rectangle(Shape):
    def __init__(self,width,hight):
        self.width = width
        self.hight = hight

    def area(self):
        return self.width * self.hight

class Square(Shape):
    def __init__(self,width):
        self.width = width

    def area(self):
        return self.width ** 2

def print_area(shape):
    print(f"площадь - {shape.area()}")

rectangle = Rectangle(3,4)
circle = Circle(5)
square = Square(7)
print_area(circle)
print_area(square)
print_area(rectangle)