#!/usr/bin/env python3
"""
Module that returns all students sorted by average score
"""
import pymongo



def top_students(mongo_collection):
    """
    Function that returns all students sorted by average score
    Args:
        mongo_collection: a pymongo collection object
    Returns:
        all students sorted by average score
    """
    if not mongo_collection:
        return []
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
