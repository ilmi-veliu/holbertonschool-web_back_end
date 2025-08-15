#!/usr/bin/env python3
"""Replace the 'topics' field for all matching school documents."""


def update_topics(mongo_collection, name, topics):
    """Set the 'topics' list for every document with the given name.

    Args:
        mongo_collection: PyMongo collection object.
        name (str): School name to match.
        topics (list of str): New topics list to set.
    """
    if mongo_collection is None:
        return
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})


if __name__ == "__main__":
    pass
