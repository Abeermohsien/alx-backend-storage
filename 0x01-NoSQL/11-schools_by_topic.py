#!/usr/bin/env python3
'''module 11.
'''


def schools_by_topic(mongo_collection, topic):
    '''list of docs
    '''
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
