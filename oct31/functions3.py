def func(a, b, c):
    print('a =', a)
    print('b =', b)
    print('c =', c)


def main():
    values = (10, 20, 30)
    func(*values)

    values_dict = {
        'b': 44,
        'c': 34,
        'a': 11
    }

    func(**values_dict)
    func(b=44, c=34, a=11)

if __name__ == '__main__':
    main()