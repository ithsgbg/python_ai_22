from re import A


def func(number):
    return number + 1


def add_10(number):
    return number + 10


def main():
    func.name = 'bob'
    print(func(10))
    print(func.name)


if __name__ == '__main__':
    main()
