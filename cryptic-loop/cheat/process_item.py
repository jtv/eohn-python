"""A few typical patterns of bad looping behaviour.

Try restructuring them.
"""
from fictional_module import (
    combobulate,
    hack,
    photograph,
    save,
    )


def find_by_id(items, id):
    """Find item with id, if any."""
    for item in items:
        if item.id == id:
            return item
    return None


def process_item(items, id):
    """Find and process the item with id; return whether it was found."""
    item = find_by_id(items, id)
    if item is None:
        return False
    else:
        hack(item)
        combobulate(item)
        save(item)
        return True


def filter_by_colour(items, colour):
    """Return just the items with colour."""
    return [
        item
        for item in items
        if item.colour == colour
        ]


def process_matches(items, colour):
    """Find and process all items with colour; return their number."""
    matches = filter_by_colour(items, colour)
    for item in matches:
        photograph(item)
        matches += 1
    return len(matches)
