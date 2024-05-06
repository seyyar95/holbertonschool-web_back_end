#!/usr/bin/python3
"""a function that lists all documents in a collection"""


def list_all(mongo_collection):
    if mongo_collection is not None:
        return list(mongo_collection.find())
    return []