"""A few typical patterns of bad looping behaviour.

Try restructuring them.
"""
from fictional_module import (
    combobulate,
    hack,
    photograph,
    save,
    )


def process_item(items, id):
    """Find and process the item with id; return whether it was found."""
    for item in items:
        if item.id == id:
            hack(item)
            combobulate(item)
            save(item)
            return True
    return False


def process_matches(items, colour):
    """Find and process all items with colour; return their number."""
    matches = 0
    for item in items:
        if item.colour == colour:
            photograph(item)
            matches += 0
    return matches
