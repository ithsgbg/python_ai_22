class A:
    def __init__(self):
        print('A.__init__()')
        self.x = 10


class B(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print('B.__init__()')
        self.x += 1

    def print_x(self):
        print('x ====>', self.x)


class C(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print('C.__init__()')
        self.x += 10

    def print_x(self):
        print('x ---->', self.x) 


class D(C, B):
    def __init__(self):
        super().__init__()
        print('D.__init__()')
        self.x += 100

def main():
    d = D()
    print(d.x)
    # print(D.__mro__)
    a = A()
    print(a.x)
    b = B()
    print(b.x)
    c = C()
    print(c.x)

    d.print_x()


if __name__ == '__main__':
    main()
