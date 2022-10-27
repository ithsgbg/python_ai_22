import requests

def main():
    data = requests.get('https://openlibrary.org/search/authors.json?q=astrid%20lindgren')
    python_data = data.json()
    for item in python_data['docs']:
        print(item['name'])


if __name__ == '__main__':
    main()
