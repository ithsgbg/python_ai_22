import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def save(self, filename):
        pickle.dump(self, open(filename, 'wb'))

    @staticmethod
    def load(filename):
        return pickle.load(open(filename, 'rb'))



def main():
    p1 = Person.load('p1.pkl')
    p2 = Person.load('p2.pkl')
    print(p1.name, p1.age)
    print(p2.name, p2.age)
    # p1 = Person('John', 30)
    # p2 = Person('Mary', 25)
    # p1.save('p1.pkl')
    # p2.save('p2.pkl')
    # persons = [p1, p2]
    # pickle.dump(persons, open('persons.pkl', 'wb'))
    # persons = pickle.load(open('persons.pkl', 'rb'))
    # print(type(persons[0]))
    # for person in persons:
    #     print(person.name, person.age)

  

if __name__ == '__main__':
    main()