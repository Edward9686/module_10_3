import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            popolnenie = random.randint(50, 500)
            with self.lock:
                self.balance += popolnenie
                print(f"Пополнение: {popolnenie}. Баланс: {self.balance}")

            time.sleep(0.001)

    def take(self):
        for i in range(100):
            snyatie = random.randint(50, 500)
            print(f"Запрос на {snyatie}")

            with self.lock:
                if snyatie <= self.balance:
                    self.balance -= snyatie
                    print(f"Снятие: {snyatie}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")

            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
