#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    n = len(boxes)

    if n == 0:
        return True

    lockboxes_open = []

    for i in range(0, n):
        lockboxes_open.append(False)

    lockboxes_open[0] = True
    unlock_box(boxes, lockboxes_open, 0)

    return all(lockboxes_open)


def unlock_box(boxes, lockboxes_open, nBox):
    """Unlock lockboxes."""
    for key in boxes[nBox]:
        if key < len(boxes) and lockboxes_open[key] is False:
            lockboxes_open[key] = True
            unlock_box(boxes, lockboxes_open, key)
