#! /usr/bin/env python
"""Here's how I would handle these errors.

The fatal errors are caught and reported all the way at the top.  In a web
application, you'd put this in your view code.  In a desktop app, you might
have it in your main handler for a user request.  It minimises the number of
places where you need error-handling code.

Two strategies will help with the recoverable errors:

What about unexpected errors?  It's often fine to let them propagate all the
way out of your code, so the runtime will report them.
"""

from random import randint
from sys import exit


class TotalFailure(Exception):
    """Exception class: something went horribly wrong.  Fail."""


class SurvivableFailure(Exception):
    """Some kind of error from which you know how to recover."""


def give_up(exception):
    """Report exception, and stop."""
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
    try:

        try:
            foo()
        except SurvivableFailure:
            recover_from_foo_failure()

        try:
            bar()
        except SurvivableFailure:
            recover_from_bar_failure()

        try:
            szut()
        except SurvivableFailure:
            recover_from_szut_failure()

    except TotalFailure as error:
        give_up(error)
    except SurvivableFailure as error:
        print("Whoa!  We failed to handle this recoverable error: %s" % error)
        exit(2)

    print("Yay!  We finished our job!")


# Even Python needs boilerplate sometimes.  It says: "do this, but only if this
# script is actually being invoked."  Someone might import the script as a
# module, and in that case, this won't run.
if __name__ == '__main__':
    main()
