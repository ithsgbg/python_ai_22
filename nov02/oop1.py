import json

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person("{self.name}", {self.age})'

    def __str__(self):
        return json.dumps(self.__dict__)

    def __gt__(self, other):
        return self.age > other.age
    
    def __ge__(self, other):
        return self.age >= other.age
    

    def reverse_name(self):
        return self.name[::-1]


def main():
    p1 = Person("Alice", 34)
    p2 = Person("Bob", 45)
    print(repr(p2))
    print(p1.reverse_name())
    print(p2.reverse_name())

    if p1 >= p2:
        print('p1 is younger')
    else:
        print('p2 is younger')

    # p1.__dict__['age'] = 34
    # print(p1.__dict__)
    # print(p2.__dict__)
    # print(p1.name, p1.age)
    # print(p1.__name)
    # p1.__name = "Lisa"
    # print(p1.__name)
    # print(p1._Person__name)
    # print(p2.__name)


if __name__ == '__main__':
    main()
