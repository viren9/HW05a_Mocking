def classify_triangle(var1, var2, var3):
    """Check the triangle"""

    if var1 == var2 == var3:
        return 'Equilateral Triangle'

    elif var1 == var2 or var1 == var3 or var2 == var3:
        return "Isosceles Triangle"

    elif var1*var1 + var2*var2 == var3*var3:
        return "Right Angled Triangle"

    elif var1 != var2 or var2 != var3:
        return "Scalene Triangle"

def main():
    """Calls the main function"""
    var1 = int(input("Enter the length of side 1 : "))
    var2 = int(input("Enter the length of side 2 : "))
    var3 = int(input("Enter the length of side 3 : "))

    print(classify_triangle(var1, var2, var3))

if __name__ == '__main__':
    main()
