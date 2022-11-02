class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

def main():
    p1 = Point(20, 40)
    p2 = Point(10, 30)

    print(p1)
    print(p2)

    p3 = p1 + p2
    print(p3)


if __name__ == '__main__':
    main()
