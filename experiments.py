from pywinauto import application
from time import sleep


app = application.Application()
app.start('Notepad.exe')
app.Notepad.menu_select("Файл->Открыть")
app.Открыть.Edit.set_edit_text('test.txt')
app.Открыть.Открыть.click(double=True)
print(app.Notepad.Edit.window_text())
sleep(5)
