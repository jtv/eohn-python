#! /usr/bin/env python
"""A script, with errors that can happen in various places.

Some of the failures come with ways to recover.  Can you find the right
combination of try/except blocks to handle and report errors nicely?  Some are
recoverable, and you should recover those.  Others are not, and we just want an
error message for those.

What happens when some completely different exception happens?
"""

from random import randint
from sys import exit


class TotalFailure(Exception):
    """Exception class: something went horribly wrong.  Fail."""


class SurvivableFailure(Exception):
    """Some kind of error from which you know how to recover."""


def give_up(exception):
    """Helper: Report exception, and stop."""
    print(exception)
    exit(1)


def foo():
    """A function that sometimes fails totally."""
    if randint(0, 5) == 0:
        raise TotalFailure("'foo' exploded.  Boy, are you unlucky today.")


def bar():
    """Work that sometimes goes wrong, sometimes fatally."""
    if randint(0, 3) == 0:
        raise SurvivableFailure(
            "Something in 'bar' went wrong, but you'll survive.")
    if randint(0, 5) == 0:
        raise TotalFailure("Tried 'bar'.  It's not working.")


def recover_from_bar_failure():
    """Deal with a failure in bar."""
    print("Well, 'bar' failed, slightly, but I fixed it.")


def szut():
    """Another complex function with different failure modes."""
    argh()
    if randint(0, 2) == 0:
        raise SurvivableFailure(
            "Oops, 'szut' broke.  But you know how to fix this.")


def argh():
    """This sometimes fails fatally."""
    if randint(0, 5) == 0:
        raise TotalFailure("In 'argh': KABOOM!")


def recover_from_szut_failure():
    """Deal with a failure in szut."""
    print("Drat, 'szut' broke, but I'm OK now.")


def main():
    """Main entry point."""
    foo()
    bar()
    szut()
    print("Yay!  We finished our job!")


# Even Python needs boilerplate sometimes.  It says: "do this, but only if this
# script is actually being invoked."  Someone might import the script as a
# module, and in that case, this won't run.
if __name__ == '__main__':
    main()
