import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skyPro", "SkyPro"),
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("привет", "Привет")
   ])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!a", "!a"),
    ("HELLO", "HELLO"),
    ("hEllO", "HEllO"),
    ("helLo", "HelLo")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" user", "user"),
    ("     @name", "@name"),
    ("      123", "123"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (" \tf23", "\tf23"),
    ("", ""),
    ("Test  ", "Test  "),
    ("  ", ""),
    ("&\n5", "&\n5"),
   ])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("test", "e", True),
    ("tesT", "T", True),
    ("Test1", "1", True),
    ("Name - Anna", "-", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str,symbol, expected", [
    ("test", "E", False),
    ("Test", "6", False),
    ("13454", "a", False),
    ("tesT", "t", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("task", "k", "tas"),
    ("12334", "3", "124"),
    ("<b>red", "<b>", "red"),
    ("Na me Ali sa  ", " ", "NameAlisa")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Small", "t", "Small"),
    ("012345", "ov", "012345"),
    ("@!#", "&", "@!#"),
    ("TEST", "s", "TEST"),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
