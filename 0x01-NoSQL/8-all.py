#!/usr/bin/env python3
'''module 8
'''


def list_all(mongo_collection):
    '''shows all docs
    '''
    return [doc for doc in mongo_collection.find()]
