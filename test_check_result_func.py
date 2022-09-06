from challenge_desktop import check_result
import pytest

@pytest.mark.parametrize('rand_string, result, expected_result', [('242141', '242141', 'PASS'), ('21412', '21451512', 'FALL'), ('45215', '', 'EMPETY')])
def test_check_result_good(rand_string, result, expected_result):
    assert check_result(rand_string, result) == expected_result