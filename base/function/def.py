
"""
def 是 Python 中的一个关键字，用于定义函数。使用 def 关键字可以创建一个新的函数对象，并将其赋予一个名称。函数的定义包括函数名、参数列表和函数体。
"""

def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

def print_shape_info(width, height):
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    print(f"Width: {width}, Height: {height}")
    print(f"Area: {area}, Perimeter: {perimeter}")

shapes = [
    {"width": 5, "height": 10},
    {"width": 3, "height": 4},
    {"width": 7, "height": 8}
]

for shape in shapes:
    print_shape_info(shape["width"], shape["height"])
    print("----")