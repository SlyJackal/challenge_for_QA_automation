#Разработать кастомное исключение и вызвать его.
#При вызове исключения оно должно содержать человекочитаемое понятное сообщение.

class ACheckException(Exception):
    """Вызывается когда зарплата сликшом маленькая или большая"""
    def __init__(self, a, message=f"A должна быть равна 2"):
        self.a = a
        self.message = f'{message}\nФактический: a = {a}'
        super().__init__(self.message)
        pass

def check_a(a):
    if a != 2:
        raise ACheckException(a)
    print(f'A = {a}')

check_a(3)