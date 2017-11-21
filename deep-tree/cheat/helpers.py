"""Helpers for tests.

These are just here to make it a little easier to write tests.
"""
import os.path
from random import randint
from shutil import rmtree
from tempfile import mkdtemp


def make_string(prefix='name', sep='-'):
    """Return an arbitrary string that is probably unique.

    :param prefix: A recognisable prefix that the name should start with.
        Use this to get random names that are still easy to trace back to a
        variable or parameter in your test.
    :param sep: Separator between the prefix and the random part of the name.
    """
    return '%s%s%d' % (prefix, sep, randint(0, 100000))


def make_temp_file(testcase, name=None):
    """Return a path for a temporary file.

    :param testcase: The TestCase containing your test.  It will be made to
        clean up the file once done.
    :param name: Optional name for the file.  If omitted, I'll make one up.
    """
    if name is None:
        name = make_string('file')
    directory = mkdtemp()
    testcase.addCleanup(rmtree, directory, ignore_errors=False)
    return os.path.join(directory, name)
