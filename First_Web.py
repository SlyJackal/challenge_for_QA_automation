'''
Реализовать программу запускающую задачи(потоки threads) через заданный интервал времени.
После завершения работы потока он должен снова запускаться через заданный интервал.
Интервал времени и название задачи указываются в конструкторе класса.
Реальная работа потока имитируется случайным ожиданием и выводом названия перед завершением работы.
'''

import random
from time import sleep
import threading

#Интервал времени и название задачи указываются в конструкторе класса.
class My_task:
    def __init__(self, name, timer):
        #выводом названия перед завершением работы - имя потока
        self.name = name
        #После завершения работы потока он должен снова запускаться через заданный интервал.
        self.timer = timer

    #Реальная работа потока имитируется случайным ожиданием и выводом названия перед завершением работы.
    def thread_activity(self):
        #cлучайное ожидание
        sleep(random.randint(1, 4))
        #выводом названия перед завершением работы
        print(self.name, 'закончил')    

#создание задач
tasks = [My_task('Name_1', 1), My_task('Name_2', 2), My_task('Name_3', 3)] 

#функции циклов создания потоков с задачами
def thread_one():
    while True:
        x = threading.Thread(target=tasks[0].thread_activity)
        x.start()
        x.join()
        sleep(tasks[0].timer)

def thread_two():
    while True:
        x = threading.Thread(target=tasks[1].thread_activity)
        x.start()
        x.join()
        sleep(tasks[1].timer)

def thread_three():
    while True:
        x = threading.Thread(target=tasks[2].thread_activity)
        x.start()
        x.join()
        sleep(tasks[2].timer)

#запуск главных потоков для функций
y_1 = threading.Thread(target=thread_one)
y_1.start()

y_2 = threading.Thread(target=thread_two)
y_2.start()

y_3 = threading.Thread(target=thread_three)
y_3.start()