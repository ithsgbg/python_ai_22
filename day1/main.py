def add_value(name, names=[]):
    names.append(name)
    return names


def main():
    print(add_value('Anna'))

    print(add_value('Bob'))

    print(add_value('Calle'))


if __name__ == '__main__':
    main()