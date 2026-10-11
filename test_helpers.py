"""
test_helpers.py - YOUR Lab 4 file.

Write at least 15 unit tests for the functions in helpers.py.
Do NOT edit helpers.py. Four worked examples are provided below so you
can see each style. Replace/extend them, then work through the TODO list.

Run:  python -m pytest -v
"""

from datetime import date

import pytest

from helpers import (
    add_days,
    days_between,
    format_currency,
    is_business_day,
    is_valid_email,
    is_valid_priority,
    slugify,
    truncate_title,
)


# ---------------------------------------------------------------
# EXAMPLE 1: a plain test with assert
# ---------------------------------------------------------------
def test_format_currency_zero():
    assert format_currency(0) == "$0.00"


# ---------------------------------------------------------------
# EXAMPLE 2: a parameterized test (many inputs, one test body)
# ---------------------------------------------------------------
@pytest.mark.parametrize(
    "value,expected",
    [
        (1, True),
        (5, True),
        (0, False),
        (6, False),
    ],
)
def test_is_valid_priority(value, expected):
    assert is_valid_priority(value) == expected


# ---------------------------------------------------------------
# EXAMPLE 3: tests grouped in a class (a test suite)
# ---------------------------------------------------------------
class TestAddDays:
    def test_add_positive_days(self):
        assert add_days(date(2026, 1, 1), 10) == date(2026, 1, 11)


# ---------------------------------------------------------------
# EXAMPLE 4: checking that an error is raised
# ---------------------------------------------------------------
def test_format_currency_rejects_text():
    with pytest.raises(TypeError):
        format_currency("free")


# ---------------------------------------------------------------
# TODO - your tests start here (aim for 15 or more in total)
#
#  [ ] format_currency: negative amount, large number (1234567),
#      a decimal that needs rounding
#  [ ] truncate_title: shorter than limit, exactly at limit,
#      one over limit (boundary), empty string, non-string input
#  [ ] slugify: spaces, special characters, repeated spaces, empty string
#  [ ] days_between: same date, later date, reversed order (negative),
#      across a year boundary
#  [ ] is_business_day: a Monday, a Friday, a Saturday, a Sunday
#      (use ONE parameterized test)
#  [ ] add_days: negative days, crossing a month end, leap day
#  [ ] is_valid_email: valid, no "@", no domain, empty string, None
#  [ ] is_valid_priority: add -1, 2.5, "3" and True (all invalid)
#  [ ] Put the tests for each function in its own Test* class
# ---------------------------------------------------------------
