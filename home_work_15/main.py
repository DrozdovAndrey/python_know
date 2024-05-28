import argparse
from Rectangle import Rectangle

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create Rectangle')
    parser.add_argument('param', metavar='width height', type=int, nargs=2,
                        help='enter width height separated by a space')

    args = parser.parse_args()
    r6 = Rectangle(*args.param)
    print(r6)

    r2 = Rectangle(3, 5)
    r3 = Rectangle(15, 200)
    r2.perimeter()
    r3.area()
    r4 = r2 + r3
    r5 = r2 - r3
    var_less = r5 < r4
    var_eq = r2 == r3
    var_less_eq = r2 <= r3
    r5.width = 5
    r5.height = 3
    var_eq2 = r5 == r2
    r1 = Rectangle(1, -5)
    r5.width = -5
    r5.height = -3
