from common_notepad_test_scenario import main_test
import pytest

@pytest.mark.parametrize('path_to_app, input_result', [('C:/Windows/system32/notepad.exe', ''), ('C:/Windows/system32/notepad.exe', '!ad')])
def test_check_result_good(path_to_app, input_result):
    main_test(path_to_app, input_result)