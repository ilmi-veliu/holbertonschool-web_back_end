#!/usr/bin/env python3
"""List all documents from a MongoDB collection."""


def list_all(mongo_collection):
    """Return all documents from the collection as a list.

    If the collection is None or has no documents, return [].
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())


if __name__ == "__main__":
    pass
