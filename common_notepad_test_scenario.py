#autotest module
from pywinauto.application import Application
from time import sleep
#text_generator
from string import ascii_letters, digits
from random import randint, sample

def text_generator():
    length = randint(5, 50)
    letters_and_digits = ascii_letters + digits
    rand_string = ''.join(sample(letters_and_digits, length))
    return rand_string

def app_test(text, path_to_app, sleep_time = 2):
    app = Application().start(path_to_app)
    app.notepad.Wait('visible')
    app.notepad.edit.TypeKeys(text)
    sleep(sleep_time)
    app.kill(soft=False)

def get_result(path_to_app, sleep_time = 2):
    app = Application().start(path_to_app)
    app.notepad.Wait('visible')
    result = app.notepad.Edit.window_text()
    sleep(sleep_time)
    app.kill(soft=True)
    return result

def main_test(path_to_app, input_result):
    rand_string = text_generator()
    app_test(rand_string, path_to_app)
    result = get_result(path_to_app)
    assert result == input_result, "Textfield is not correct!"


if __name__ == "__main__":
    print("Please use test_in_pytest_test.py to launch test!")


