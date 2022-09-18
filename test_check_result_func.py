from challenge_desktop import main_test
import pytest

@pytest.mark.parametrize('path_to_app, expected_result', [('C:/Windows/system32/notepad.exe', 'FALL')])
def test_check_result_good(path_to_app, expected_result):
    assert main_test(path_to_app) == expected_result