#!/usr/bin/env python3
"""Insert a new document in a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Fuction insert a new document and return his id"""

    if mongo_collection is None:
        return None
    res = mongo_collection.insert_one(dict(kwargs))
    return res.inserted_id


if __name__ == "__main__":
    pass
