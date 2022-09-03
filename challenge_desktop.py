from pprint import pprint
from pywinauto.application import Application
from time import sleep
from string import ascii_letters, digits
from random import randint, sample

def text_generator():
    global rand_string
    length = randint(5, 50)
    letters_and_digits = ascii_letters + digits
    rand_string = ''.join(sample(letters_and_digits, length))
    return(rand_string) 


def common_notepad(text, sleep_time = 2):
    app = Application().start('notepad.exe')
    app.Notepad.Wait('visible')
    app.Notepad.edit.TypeKeys(text)
    sleep(sleep_time)
    app.kill(soft=False)


def notepadplusplus(text, sleep_time = 3):
    global app, read_text
    app = Application().start('C:/Program Files/Notepad++/notepad++.exe')
    notepad = app[u'Notepad++']
    notepad.Restore()
    notepad.Wait('ready')
    notepad.TypeKeys(text) 
    sleep(sleep_time)
    read_text = app.notepad.Edit.window_text()
    return app, read_text

def main_test():
    for i in range(0):
        text_generator()
        common_notepad(rand_string)
    for i in range(2):    
        text_generator()
        final_text = str()
        final_text += rand_string
        notepadplusplus(rand_string)
        app.kill(soft=False)
    print('!!!!!!!!!!!!!!!!!!!!!!')
    print(f'read_text = {read_text}')
    print(f'final_text = {final_text}')
    print('!!!!!!!!!!!!!!!!!!!!!!')
    eraser = '^a' + '{BACKSPACE}'
    notepadplusplus(eraser)


main_test()


