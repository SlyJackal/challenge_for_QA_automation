from pywinauto.application import Application
from time import sleep
#text_generator
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
    sleep(sleep_time)
    app.kill(soft=False)

def get_result():
    app = Application().start('notepad.exe')
    app.Notepad.Wait('visible')
    result = app.Notepad.Edit.window_text()
    if result == '':
        result = 'EMPETY'
    return result

def check_result(rand_string, result):
    if result == rand_string:
        return 'PASS'
    elif result == '':
        return 'EMPETY'
    else:
        return 'FALL'


""" def notepadplusplus(text, sleep_time = 3):
    global app, read_text
    app = Application().start('C:/Program Files/Notepad++/notepad++.exe')
    notepad = app[u'Notepad++']
    notepad.Restore()
    notepad.Wait('ready')
    notepad.TypeKeys(text) 
    sleep(sleep_time)
    result = app.Notepad.Edit.window_text()
    print('_______________________\n')
    print(f'\nResult - {result}\n')
    print('_______________________')
    return app """

""" def check_result():
    app = Application().start('C:/Program Files/Notepad++/notepad++.exe')
    notepad = app[u'Notepad++']
    notepad.menu_select("File->Save")
    notepad.Отмена.Edit.set_edit_text('test.txt')
    notepad.Да.click()
    notepad.menu_select("File->Save")
    notepad.Открыть.Открыть.click(double=True)
    print(notepad.Edit.window_text()) """

def main_test():
    result = str()
    text_generator()
    common_notepad(rand_string)
    check_result(rand_string, result)



    """ for i in range(2):    
        text_generator()
        final_text = str()
        notepadplusplus(rand_string)
        final_text += rand_string
        app.kill(soft=False)
    check_result() """
    eraser = '^a' + '{BACKSPACE}'
    


#main_test()
#check_result()
#text_generator()
#notepadplusplus(rand_string)
#common_notepad(rand_string)


