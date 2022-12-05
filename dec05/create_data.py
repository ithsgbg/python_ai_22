import datetime
from mongo_doc import init_db, create_collection_class


init_db('mongodb://localhost:27017', 'IoT')

Value = create_collection_class('Value', 'temperatures')

temps = [float(value) for value in open('./dec05/Xdados.txt', 'r').read().split()]

date  = datetime.datetime(2022, 9, 9, 0, 0, 0)

for temp in temps:
    value = {
        'date': date.strftime('%Y-%m-%d'),
        'time': date.strftime('%H:%M:%S'),
        'temperature': temp
    }
    mongo_val = Value(**value)
    mongo_val.save()
    date += datetime.timedelta(seconds=10)
