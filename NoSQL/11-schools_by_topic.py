#!/usr/bin/env python3
"""Return schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of documents whose 'topics' array contains 'topic'.

    Args:
        mongo_collection: PyMongo collection object.
        topic (str): Topic to search for.

    Returns:
        list: List of matching documents. [] if collection is None.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find({"topics": topic}))


if __name__ == "__main__":
    pass
