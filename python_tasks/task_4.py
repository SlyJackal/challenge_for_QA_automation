#Базовый уровень:
#Создайте класс представляющий из себя объект Заказ.
#Класс должен иметь аттрибуты: номер заказа, название, ФИО отправителя, адрес, статус (доставлен/не доставлен и изначально установлен статус не доставлен).
#Реализованы свойства: Изменение статуса заказа, вывод информации о заказе.
#Продвинутый уровень:
#Доработать класс с применением продвинутых возможностей работы с классами в Python, например сделать иерархию различных видов заказов, использовать модификаторы доступы для атрибутов и методов и т.д.

class OrderShop():
    __order_counter = 0
    def __init__(self, name, customer_name, adress):
        OrderShop.__order_counter += 1
        self.__order_number = OrderShop.__order_counter
        self.__name = name
        self.__customer_name = customer_name
        self.__adress = adress
        self.__delivered = False

    def __str__(self):
        if self.__delivered:
            status_deliver = 'Доставлено'
        else:
            status_deliver = 'Не доставлен'
        return f'Номер заказа - {self.__order_number}\nПолучатель - {self.__customer_name}\nАдрес доставки - {self.__adress}\nСтатус доставки - {status_deliver}'

    def set_delivered_status(self):
        self.__delivered = True 
        return f'Cтатус доставки изменен\n{str(self)}'

            
class PostpaidOrder(OrderShop):
    def __init__(self, name, customer_name, address):
        super().__init__(name, customer_name, address)
        self.__is_paid = False
    
    def __str__(self):
        paid = 'Оплачен' if self.__is_paid else 'Не оплачен'
        return f'{super().__str__()}\nСтатус оплаты - {paid}'
    
    def set_paid_status(self):
        self.__is_paid = True  



a = OrderShop('Samsung', 'Vova', 'Adress 1')
print(a)

b = PostpaidOrder('Apple', 'Julia', 'Adress 2')
print(b)