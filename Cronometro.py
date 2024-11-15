import time
import os

class Cronometro:
    def __init__(self, segundos=0, minutos=0, horas=0):
        self.segundos = segundos
        self.minutos = minutos
        self.horas = horas

    def __repr__(self):
        print(f"Hora: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}")
        time.sleep(0.1) #O valor 0.1 é colocado para que ele funcione como cronometro, não relógio.

    def incremento(self):
        self.segundos += 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos += 1
        elif self.minutos == 60:
            self.minutos = 0
            self.horas += 1

    def start(self):
        while True:
            self.__repr__()
            os.system('cls')
            self.incremento()

cronometro1 = Cronometro()
cronometro1.start()
