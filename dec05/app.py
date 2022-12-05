from fastapi import FastAPI
from mongo_doc import init_db, create_collection_class


init_db('mongodb://localhost:27017', 'IoT')
Value = create_collection_class('Value', 'temperatures')


app = FastAPI()


@app.get('/')
def index():
    return Value.random_sample()


@app.get('/date/{date}')
def get_by_date(date):
    return Value.find(**{'date': {'$eq': date}})


