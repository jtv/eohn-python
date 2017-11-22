

def get_value():
    """Obtain value."""
    # ...


def do_stuff():
    try:
        initialise()
        value = get_value()
        if value > threshold:
            report_problem(value)
    except Exception:
        # Nah.  Probably just not defined.
        value = default_value


