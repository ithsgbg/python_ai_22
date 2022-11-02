from string import ascii_letters

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        for letter in new_name:
            if letter not in ascii_letters + 'åäöÅÄÖ':
                raise ValueError(f'The name {new_name} has a character {letter}. It is not allowed in a name')
        self._name = new_name

def main():
    p1 = Person('Anna')
    print(p1.name)
    p1.name = 'Örjan'
    print(p1.name)


if __name__ == '__main__':
    main()
