"""
Задача "Банковские операции"
"""
import random
import threading
from threading import Thread, Lock
from time import sleep


class Bank(Thread):
    def __init__(self, balance, lock=Lock()):
        super().__init__()
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(0, 100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            money_in = random.randrange(50, 500)
            self.balance += money_in
            print(f'Пополнение: {money_in}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(0, 100):
            money_out = random.randrange(50, 500)
            print(f'Запрос на {money_out}')
            if money_out <= self.balance:
                self.balance -= money_out
                print(f'Снятие: {money_out}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank(0)

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
