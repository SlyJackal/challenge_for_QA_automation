'''
Реализовать программу обрабатывающую поток сообщений.
Программа обрабатывает несколько сообщений одновременно в несколько потоков.
Обработка сообщения имитируется случайным ожиданием и выводом номера сообщения после завершения.
Поток сообщения создаётся генератором python.
'''


from random import randrange, sample
from string import ascii_letters, digits

class Messages():
    def __init__(self, timer):
        #выводом сообщения
        #После завершения работы потока он должен снова запускаться через заданный интервал.
        self.timer = timer

    #Генератор сообщений.
    def message_generator():
        length = randrange(5, 50)
        letters_and_digits = ascii_letters + digits + (' ' * 10)
        rand_string = ''.join(sample(letters_and_digits, length))
        print(rand_string) 


