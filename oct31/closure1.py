def func(n):
    n += 20
    def inner_func():
        nonlocal n
        n += 1
        return n

    return inner_func


def main():
    a = func(10)
    print(a())

    b = func(100)
    print(b())
    print(b())
    print(b())
    print(b())
    print(b())
    print(b())

    print(a())
    print(a())
    print(a())
    print(a())


if __name__ == '__main__':
    main()