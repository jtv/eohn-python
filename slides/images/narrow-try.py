

class ValueNotDefined(Exception):
    """The value you're looking for was not defined."""

def get_value():
    """Obtain value.  Raise ValueNotDefined if not defined."""
    # ...


def do_stuff():
    initialise()
    try:
        value = get_value()
    except ValueNotDefined:
        value = default_value
    if value > threshold:
        report_problem(value)
    return value


