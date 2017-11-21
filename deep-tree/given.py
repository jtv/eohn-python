"""Externals for the deep-tree exercise.

These are just placeholders.  Imagine there's something much more complicated
going on here that you can't touch.
"""
from codecs import open
import json
import os.path


def read_text_file(path):
    """Read a text file.  Return its contents.

    :raise IOError: if the file could not be opened.  If the file was not
        found, its errno will be set to errno.ENOENT.
    """
    with open(path, encoding='utf-8') as f:
        return f.read()


def write_text_file(path, contents):
    """Write contents to text file at path."""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(contents)


def dump_text(text):
    """Print text to the console."""
    print(text)


def locate_config():
    """Return the location of the config file."""
    this_dir = os.path.dirname(__file__)
    return os.path.join(this_dir, 'files', 'config.json')


def parse_config_file(config_contents):
    """Parse the JSON config file contents, return as a dict."""
    return json.loads(config_contents)
