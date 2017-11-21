"""Here's a module to read and print a log file.  It's not very nice.

It's especially hard to test.  Without removing or renaming any of the
functions, can you restructure this module to make that easier?
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
    config_file = locate_config()
    config = read_config(config_file)
    log_file = locate_log(config)
    dump_text(read_log(log_file))


def read_config(config_file):
    """Read and parse the config file."""
    contents = read_text_file(config_file)
    return parse_config_file(contents)


def locate_log(config):
    """Locate the log file."""
    return config['log-location']


def read_log(log_file):
    """Get the log file's location, and read the log file."""
    return read_text_file(log_file)
