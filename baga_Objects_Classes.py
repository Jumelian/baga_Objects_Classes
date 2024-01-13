class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.calculate_area()
        self.calculate_perimeter()

    def calculate_area(self):
        self.area = 3.141592653589793 * self.radius ** 2

    def calculate_perimeter(self):
        self.perimeter = 2 * 3.141592653589793 * self.radius

    def display_info(self):
        print(f"Circle with radius:{self.radius}")
        print(f"Area:{self.area:.2f}")
        print(f"Perimeter:{self.perimeter:.2f}")
my_circle = Circle(radius= 5)
my_circle.display_info()