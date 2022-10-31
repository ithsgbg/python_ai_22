from functools import wraps


def func(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return '<<<< ' + result + ' >>>>'
    return wrapper


@func
def greeting(greet, name):
    return f'{greet}, {name}!'

@func
def say_hi(name):
    return f'Hi, {name}...'


# greeting = func(greeting)

def main():
    print(greeting('Hello', 'Alice'))
    print(greeting('Hi', 'Bob'))

    print(greeting.__name__)

    print(say_hi('Carl'))



if __name__ == '__main__':
    main()

