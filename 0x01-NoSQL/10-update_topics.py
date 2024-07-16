#!/usr/bin/env python3
'''module 10
'''


def update_topics(mongo_collection, name, topics):
    '''updaye topics.
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
