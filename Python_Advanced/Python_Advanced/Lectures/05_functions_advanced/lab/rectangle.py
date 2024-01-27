# def rectangle(length, width):
#     if isinstance(length, int) and isinstance(width, int):
#         return (f"Rectangle area: {length * width}\n"
#                 f"Rectangle perimeter: {2 * (length + width)}")
#     return "Enter valid values!"

def rectangle(length, width):
    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"

    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


# print(rectangle(2, 10))
print(rectangle('2', 10))