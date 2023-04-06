import unittest
from project1.func import redacted_names,redacted_dates,redacted_phones,redacted_genders,redact_address_data
import os
def test_redacted_names():

    input_str = "Hello, my name is John Doe. Nice to meet you."
    expected_output = "Hello, my name is ████████. Nice to meet you."

    assert redacted_names(input_str) == expected_output
def test_redacted_dates():
    sample_text = "13 Dec 1999 01:34:00"
    expected_output = "█ 01:34:00"
    assert redacted_dates(sample_text) == expected_output
def test_redacted_phones():
    sample_text = "(123) 456-7890"
    expected_output = "█"
    assert redacted_phones(sample_text) == expected_output
def test_redacted_genders():
    sample_text = "He"
    expected_output = "█"
    assert redacted_genders(sample_text)  == expected_output
def test_redact_address_data():
    sample_text = "The conference will take place at the Chicago."
    expected_output = "The conference will take place at the ███████."
    assert redact_address_data(sample_text) == expected_output

class TestRedaction(unittest.TestCase):
    
    def test_stats(self):
        # Copy and paste the contents of the test_stats function here
        pass

if __name__ == '__main__':
    unittest.main()
