#!/usr/bin/python3
''' lockboxes
'''


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all boxes can be opened.

    Parameters:
    - boxes (List[List[int]]): A list of lists where each inner list represents
 a box and contains keys.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    # Initialize a set to keep track of opened boxes
    opened_boxes = set([0])

    # Process each box and update the set of opened boxes
    for box_number, keys in enumerate(boxes):
        if box_number in opened_boxes:
            opened_boxes.update(keys)

    # Check if all boxes are opened
    return len(opened_boxes) == len(boxes)
