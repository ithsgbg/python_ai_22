"""
Mongo Doc Library
~~~~~~~~~~~~~~~~~~
A simple and easy to use library to access a MongoDB database.

Basic usage:
from mongo_doc import init_db, create_collection_class


# First initialize the database connection
init_db('mongodb://username:password@host:port')


# Create a collection class
User = create_collection_class('User', 'users')

# Create a user object
user = User(**
    {
        'first_name': 'Alice',
        'last_name': 'Smith',
        'email': 'alice@email.com'
    })

# Save the object to the database
user.save()

# Search for all users with this first name and return the first hit
# or None if no documents are found
user = User.find(first_name='Alice').first_or_none()
if user:
    # Change the first name
    user.first_name = 'Bob'
    # and save it
    user.save()

:copyright: (c) 2022 by Joakim Wassberg.
:license: Apache 2.0, see LICENSE for more details.
:version: 0.02
"""
from copy import copy
from typing import Union
import bson
from pymongo import MongoClient


# The __db object needs to be initialized before the library can be used
_db = None


# *******************
# Library exceptions
# *******************
class MongoException(Exception):
    """
    Base exception class
    """
    pass


class MongoInitError(MongoException):
    """
    Database initialization exceptions
    """
    pass


class MongoCollectionError(MongoException):
    """
    Collection exceptions
    """
    pass

class MongoFieldError(MongoException):
    """
    Field exceptions
    """
    pass


class ResultList(list):
    """
    Extends the list class with methods to retrieve the first or last value, or None if the list is empty
    This class is used as a return value for returned documents
    """
    def first_or_none(self):
        """
        Return the first value or None if list is empty
        :return: First list element or None
        """
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        """
       Return the last value or None if list is empty
       :return: Last list element or None
       """
        return self[-1] if len(self) > 0 else None


class Document(dict):
    """
    This class acts as the base class for collection classes. Each instance of the subclasses
    will represent a single document
    """
    collection = None

    def __init__(self, **kwargs):
        super().__init__()
        # If _id is not present we add the _id attribute
        if '_id' not in kwargs:
            self._id = None

        # We need to check if there is an embedded document in this document.
        # If so, we will convert it into a dict
        d = copy(kwargs)
        for k, v in kwargs.items():
            if isinstance(v, Document):
                d[k] = v.__dict__

        # Update the object
        self.__dict__.update(d)

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def to_dict(self) -> dict:
        if '_id' in self.__dict__:
            self._id = str(self._id)
        return self.__dict__

    def _get_auto_id(self, sequence_name: str, increment: int=2) -> int:
        """
        Gives you an auto increment field in mongodb
        Works with a collection in your mongodb that needs to have the name
        counters.
        Each document needs to in the form:
        {
            "_id": "sequence_name",
            "sequence_value": 0
        }

        The _id needs to be a unique value per sequence you need to work with, defined as a string.
        The sequence_value is the starting value for the auto increment

        :param sequence_name: str - The name of the sequence to use (mathing the _id)
        :param increment: int - Optional, how much to increment the value each time. Default value is 2
        :return: int - The next value from the auto increment
        """
        if 'counters' not in _db.list_collection_names():
            raise MongoCollectionError('To use an auto increment field you need a collection called counters.')
        
        updated_record = _db.counters.find_one_and_update(
            filter = {"_id": sequence_name},
            upsert = True, 
            update = {"$inc": {"sequence_value": increment}},
            return_document=True
        )
        return updated_record['sequence_value']

    def save(self, auto_field=None, auto_key=None):
        """
        Saves the current object to the database
        :param auto_field: str | None, if using auto increment key, the name of the key field
        :param auto_key: str | None, name of the key used in counters collection for this auto increment 
        :return: The saved object
        """
        if auto_field:
            if not auto_key:
                raise MongoFieldError('To use auto field, an auto key must be provided')
            self.__dict__[auto_field] = self._get_auto_id(auto_key)

        # If _id is None, this is a new document
        if self._id is None:
            del (self.__dict__['_id'])
            return self.collection.insert_one(self.__dict__)
        else:
            return self.collection.replace_one({'_id': self._id}, self.__dict__)

    def delete_field(self, field):
        """
        Removes a field from this document
        :param field: str, the field to remove
        :return: None
        """
        self.collection.update_one({'_id': self._id}, {"$unset": {field: ""}})

    @classmethod
    def get_by_id(cls, _id):
        """
        Get a document by its _id
        :param _id: str, the id of the document
        :return: The retrieved document or None
        """
        try:
            return cls(cls.collection.find_one({'_id': bson.ObjectId(_id)}))
        except bson.errors.InvalidId:
            return None

    @classmethod
    def insert_many(cls, items):
        """
        Inserts a list of dictionaries into the databse
        :param items: list of dict, items to insert
        :return: None
        """
        for item in items:
            cls(item).save()

    @classmethod
    def all(cls):
        """
        Retrieve all documents from the collection
        :return: ResultList of documents
        """
        return ResultList([cls(**item) for item in cls.collection.find({})])

    @classmethod
    def all_iter(cls):
        """
        Retrieve all documents from the collection
        :return: ResultList of documents
        """
        for item in cls.collection.find({}):
            yield cls(**item).to_dict()

    @classmethod
    def find(cls, **kwargs):
        """
        Find a document that matches the keywords
        TODO: Let user pass in a dict as well
        :param kwargs: keyword arguments to match
        :return: ResultList
        """
        return ResultList(cls(**item).to_dict() for item in cls.collection.find(kwargs))

    @classmethod
    def delete(cls, **kwargs):
        """
        Delete the document that matches the keywords
        TODO: Let user pass in a dict as well
        :param kwargs: keyword arguments to match
        :return: None
        """
        cls.collection.delete_many(kwargs)

    @classmethod
    def document_count(cls):
        """
        Returns the total number of documents in the collection
        :return: int
        """
        return cls.collection.count_documents({})

    @classmethod
    def random_sample(cls, size=10):
        pipe = [
            {
                "$sample": {
                    "size": size
                }
            }
        ]
        return ResultList(cls(**item).to_dict() for item in cls.collection.aggregate(pipe))

# *******************
# Helper functions
# *******************

def create_collection_class(class_name: str, collection_name: Union[str, None] = None):
    """
    Factory function for creations of collection classes
    :param class_name: str, name of collection class
    :param collection_name: str or None, name of collection in database. If None, the class name will be used
    :return: The newly created collection class
    """
    if collection_name is None:
        collection_name = class_name

    if _db is None:
        raise MongoInitError('init_db function must be called before creation of collection classes')
    collection_class = type(class_name, (Document, ), {
        'collection': _db[collection_name]
    })
    return collection_class


def add_collection_method(cls, method):
    """
    Helper function to add methods to a collection class.
    Usage:
    def method(self):
        print(self.name)

    user = create_collection_class('User')
    add_collection_method(User, method)
    user.method()
    :param cls: The collection class
    :param method: The method to add to the class
    :return: None
    """
    setattr(cls, method.__name__, method)


def init_db(connection_str, database):
    """
    Function to initialize database connection. Must be called before any use of the library
    :param connection_str: str, the database connection string
    :param database: str, the name of the database to use
    :return: None
    """
    client = MongoClient(connection_str)
    global _db
    _db = client[database]