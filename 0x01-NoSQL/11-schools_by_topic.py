#!/usr/bin/env python3
"""
Module that returns the list of school having a specific topic
"""
import pymongo


def update_topics(mongo_collection, topic):
    """
    Function that changes all topics of a school document based on the name

    Args:
        mongo_collection: a pymongo collection object
        topics: list of topics approached in the school
    """
    if not mongo_collection:
        return None
    return mongo_collection.find({"topics": topic})
