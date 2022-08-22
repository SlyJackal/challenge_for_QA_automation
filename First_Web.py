'''
Реализовать программу запускающую задачи(потоки threads) через заданный интервал времени.
После завершения работы потока он должен снова запускаться через заданный интервал.
Интервал времени и название задачи указываются в конструкторе класса.
Реальная работа потока имитируется случайным ожиданием и выводом названия перед завершением работы.
---------------------------
Сделай так чтоб завершалась и запускался новый поток.
'''

from random import randint
from time import sleep
from threading import Thread

#Установка границ генерации количества задач
range_of_tasks_start = 4
range_of_tasks_finish = 10

#Установка границ времени ожидания активности
range_of_activity_start = 1
range_of_activity_finish = 4

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
        sleep(randint(range_of_activity_start, range_of_activity_finish))
        #выводом названия перед завершением работы
        print(f'{self.name} закончил')    

#список задач
tasks = [My_task('Name_1', 1), My_task('Name_2', 2), My_task('Name_3', 3)] 

#функции циклов создания потоков с задачами
def thread_common(task):
    numbers_of_tasks = randint(range_of_tasks_start, range_of_tasks_finish)   
    threads = list()
    for i in range(numbers_of_tasks):
        threads.append(Thread(target=task.thread_activity))
        threads[i].start()
        threads[i].join()
        sleep(task.timer)
        
#спиcок потоков
flows = list()

#запуск главных потоков для функций
for i in range(0, len(tasks)-1):   
    flows.append(Thread(target=thread_common(tasks[i])))
for flow in flows:
    flows[i].start()
    flows[i].join()

