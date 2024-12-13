import pytest
import json
import re
import email_domain_sorter as email

def test_valid():
    assert email.fill_special_domains("test_files/valid_special_domains.json") == {"hello":["test"]}

def test_invalid_specialdomain():
    # Test invalid json syntax in file
    with pytest.raises(json.decoder.JSONDecodeError):
        email.fill_special_domains("test_files/invalid_special_domains_1.json")

    # test no file exists
    with pytest.raises(FileNotFoundError):
        email.fill_special_domains("")

def test_invalid_emails():
    # test many @'s
    with pytest.raises(ValueError):
        email.create_domains(["@@@@"], email.fill_special_domains("special_domains.json"))

    # test just .com
    with pytest.raises(ValueError):
        email.create_domains([".com"], email.fill_special_domains("special_domains.json"))