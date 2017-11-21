"""Here's a module to read and print a log file.

It's not very nice.  The only things we need to keep unchanged are the API for
print_log, and the helpers in the "given" module.

The code is especially hard to test.  Can you restructure it to fix that?
"""
from given import (
    dump_text,
    locate_config,
    parse_config_file,
    read_text_file,
    )


def print_log():
    """Main entry point.  Locate and dump a log file.

    The log file's location is stored in a config file.  The config file is a
    bit hard to find.  Call location_config to get its location.
    """
    text = read_log()
    dump_text(text)


def read_log():
    """Get the log file's location, and read the log file."""
    log_file = locate_log()
    return read_text_file(log_file)


def locate_log():
    """Locate the log file."""
    config_file = locate_config()
    config = read_text_file(config_file)
    parsed_config = parse_config_file(config)
    return parsed_config['log-location']
