import requests


# data = requests.get('http://localhost:8000/date/2022-10-14').json()
# for item in data:
#     print(item['date'], item['time'], item['temperature'])

number = input('Enter a number to check: ')
data = requests.get('http://numbersapi.com/' + number).text
print('Fun fact about', number)
print(data)