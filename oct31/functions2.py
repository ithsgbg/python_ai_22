def func1(a, b, *args, **kwargs):
    print(f'func1 called with {len(args)} positional arguments')
    for value in args:
        print(value)

    print(kwargs)


def main():
    # func1()
    # func1(1)
    func1(1, 2)
    func1(1, 2, 'aha')
    func1(1, 2, 'aha', name='Anna', age=34, email='anna@email.com')
    func1(1, 2, nickname='Bob')


if __name__ == '__main__':
    main()
