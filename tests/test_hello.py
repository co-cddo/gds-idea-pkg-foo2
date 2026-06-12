"""Tests for the hello function."""

from foo2 import hello


def test_hello_default():
    """hello() returns a greeting with default name."""
    assert hello() == "Hello, world!"


def test_hello_with_name():
    """hello(name) returns a greeting with the given name."""
    assert hello("foo2") == "Hello, foo2!"
