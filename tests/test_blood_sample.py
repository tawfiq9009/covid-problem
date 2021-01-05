
from src.blood_sample import BloodSample


def test_create_a_valid_patient_row():
    input = '0110001110'
    sample = BloodSample(input)
    assert sample.is_valid()


def test_create_invalid_patient_row():
    input = '0110001112'
    sample = BloodSample(input)
    assert not sample.is_valid()


def test_parse_valid_row():
    input = '0110001110'
    sample = BloodSample(input)
    assert sample.parse() == ['11', '111']


def test_result_of_valid_row():
    input = '0110001110'
    sample = BloodSample(input)
    sample.parse()

    assert sample.number_of_matched == 2
    assert sample.list_of_matched == [2, 3]
