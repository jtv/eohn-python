"""Tests for deep_tree.

We'll try to test every function in detail.
"""
from deep_tree import (
    locate_log,
    print_log,
    read_log,
    )
from given import write_text_file
from helpers import (
    make_temp_file,
    make_string,
    )
import json
from mock import patch
from unittest import TestCase


class TestPrintLog(TestCase):
    """Tests for top-level function."""
    def test_end_to_end(self):
        # Create a fake log file.
        fake_log = make_temp_file(self, 'fake.log')
        contents = make_string("Log content", sep=' ')
        write_text_file(fake_log, contents)

        # Inject a fake config pointing to the fake log file.
        fake_config = make_temp_file(self, 'config.json')
        config_contents = json.dumps({'log-location': fake_log})
        write_text_file(fake_config, config_contents)

        # Temporarily patch deep_tree's imported copy of dump_text.
        # Replace it with a Mock, a magic test double.
        with patch('deep_tree.dump_text') as fake_dump:
            print_log()

        # A Mock records its calls in call_args_list.  It got one.
        [call] = fake_dump.call_args_list

        self.assertEqual(call.args, (contents,))


class TestReadLog(TestCase):
    """Tests for read_log."""
    def test_returns_log_contents(self):
        self.fail("TODO: Test this.")

    def test_raises_IOError_if_file_not_found(self):
        self.fail("TODO: Test this.")


class TestLocateLog(TestCase):
    """Tests for locate_log."""
    def test_returns_config_file_entry(self):
        self.fail("TODO: Test this.")
