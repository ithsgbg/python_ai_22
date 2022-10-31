def func1(a: int, b=50, c=60):
    print(id(a))
    a.append(4)
    print(id(a))
    print('a =', a)
    print('b =', b)
    print('c =', c)


def main():
    x = [1, 2, 3]
    print(id(x))
    func1(x, c=10, b=34)
    print(id(x))
    print(x)


if __name__ == '__main__':
    main()