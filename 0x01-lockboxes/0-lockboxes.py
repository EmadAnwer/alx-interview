#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    keys = set()
    keys.add(0)
    for i in range(len(boxes)):
        for key in boxes[i]:
            if (key > i or key < i):
                keys.add(key)
    return len(boxes) == len(keys)
