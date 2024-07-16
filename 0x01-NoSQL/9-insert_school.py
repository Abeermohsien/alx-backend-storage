#!/usr/bin/env python3
'''module 9.
'''


def insert_school(mongo_collection, **kwargs):
    '''add new doc.
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
